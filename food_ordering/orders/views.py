from django.shortcuts import render, redirect, get_object_or_404
from .models import OrderItem, Order
from cart.cart import Cart

def order_create(request):
    cart = Cart(request)
    if not cart: # redirect empty cart
        return redirect('cart:cart_detail')
        
    if request.method == 'POST':
        # Simple processing of form without Django Forms for rapid implementation
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
            city=city
        )
        
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
        
        # clear the cart
        cart.clear()
        # redirect to the tracking view
        return redirect('orders:order_tracking', order_id=order.id)
    else:
        return render(request, 'orders/checkout.html', {'cart': cart})

def order_tracking(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/tracking.html', {'order': order})
