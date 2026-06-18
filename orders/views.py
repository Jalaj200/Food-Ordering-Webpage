from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
import razorpay
import logging
from .models import OrderItem, Order
from cart.cart import Cart

logger = logging.getLogger(__name__)

def order_create(request):
    cart = Cart(request)
    if not cart: # redirect empty cart
        return redirect('cart:cart_detail')
        
    delivery_fee = Decimal('40.00')
    taxes = Decimal(cart.get_total_price()) * Decimal('0.05')
    
    # Check if user has an address we can prepopulate
    default_address = None
    if request.user.is_authenticated:
        default_address = request.user.addresses.filter(is_default=True).first()
        if not default_address:
            default_address = request.user.addresses.first()

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        postal_code = request.POST.get('postal_code')
        city = request.POST.get('city')
        
        order = Order.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            address=address,
            postal_code=postal_code,
            city=city,
            delivery_fee=delivery_fee,
            taxes=taxes
        )
        
        if request.user.is_authenticated:
            order.user = request.user
            order.save()
            
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
            
        # Initialize Razorpay Client
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        
        # Create Razorpay Order
        payment_data = {
            "amount": int(order.get_total_cost() * 100), # Amount in paise
            "currency": "INR",
            "payment_capture": "0" # Manual capture or auto. Standard is to verify signature first
        }
        
        # Validate API Keys
        if not settings.RAZORPAY_KEY_ID or settings.RAZORPAY_KEY_ID == 'rzp_test_your_key_id_here' or 'your_key_id_here' in settings.RAZORPAY_KEY_ID:
            messages.error(request, "Payment Gateway Setup Required: Please add your real Razorpay API Keys to the .env file and restart your server.")
            logger.error("Razorpay API Keys are missing or set to default placeholder in .env file.")
            return redirect('cart:cart_detail')

        try:
            razorpay_order = client.order.create(data=payment_data)
            order.razorpay_order_id = razorpay_order['id']
            order.payment_method = 'Razorpay'
            order.save()
            logger.info(f"Successfully created Razorpay order {razorpay_order['id']} for local order {order.id}")
        except razorpay.errors.BadRequestError as e:
            logger.error(f"Razorpay Bad Request: {str(e)}", exc_info=True)
            messages.error(request, f"Payment gateway error: {str(e)}")
            return redirect('cart:cart_detail')
        except razorpay.errors.GatewayError as e:
            logger.error(f"Razorpay Gateway Error: {str(e)}", exc_info=True)
            messages.error(request, "Payment gateway is currently down. Please try again later.")
            return redirect('cart:cart_detail')
        except razorpay.errors.ServerError as e:
            logger.error(f"Razorpay Server Error: {str(e)}", exc_info=True)
            messages.error(request, "Payment gateway server error. Please try again later.")
            return redirect('cart:cart_detail')
        except Exception as e:
            logger.error(f"Razorpay Order Creation Failed unexpectedly: {str(e)}", exc_info=True)
            messages.error(request, f"Error communicating with payment gateway: {str(e)}")
            return redirect('cart:cart_detail')

        return redirect('orders:payment', order_id=order.id)
    else:
        context = {
            'cart': cart, 
            'delivery_fee': delivery_fee, 
            'taxes': taxes,
            'grand_total': cart.get_total_price() + delivery_fee + taxes,
            'default_address': default_address
        }
        return render(request, 'orders/checkout.html', context)

def payment_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    # Basic security check
    if order.user and order.user != request.user:
        messages.error(request, "You do not have permission to view this order.")
        return redirect('menu:menu_list')
        
    if order.payment_status == 'Paid':
        return redirect('orders:success', order_id=order.id)

    context = {
        'order': order,
        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
        'amount_in_paise': int(order.get_total_cost() * 100)
    }
    return render(request, 'orders/payment.html', context)

@csrf_exempt
def payment_verify(request):
    if request.method == "POST":
        razorpay_payment_id = request.POST.get('razorpay_payment_id', '')
        razorpay_order_id = request.POST.get('razorpay_order_id', '')
        razorpay_signature = request.POST.get('razorpay_signature', '')
        
        order = get_object_or_404(Order, razorpay_order_id=razorpay_order_id)
        
        # Prevent duplicate payment processing
        if order.payment_status == 'Paid':
            logger.warning(f"Duplicate payment verification attempt for order {order.id}")
            return redirect('orders:success', order_id=order.id)
            
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': razorpay_signature
        }
        
        try:
            client.utility.verify_payment_signature(params_dict)
            # Signature verified
            order.razorpay_payment_id = razorpay_payment_id
            order.razorpay_signature = razorpay_signature
            order.payment_status = 'Paid'
            order.status = 'Confirmed'
            order.save()
            
            # Clear the cart now that payment is successful
            cart = Cart(request)
            cart.clear()
            
            return redirect('orders:success', order_id=order.id)
            
        except razorpay.errors.SignatureVerificationError:
            order.payment_status = 'Failed'
            order.save()
            return redirect('orders:failure', order_id=order.id)
            
    return redirect('menu:menu_list')

def payment_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if order.user and order.user != request.user:
        return redirect('menu:menu_list')
    return render(request, 'orders/success.html', {'order': order})

def payment_failure(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if order.user and order.user != request.user:
        return redirect('menu:menu_list')
    return render(request, 'orders/failure.html', {'order': order})

def order_tracking(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/tracking.html', {'order': order})
