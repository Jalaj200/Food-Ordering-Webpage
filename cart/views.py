from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from menu.models import MenuItem
from .cart import Cart

@require_POST
def cart_add(request, item_id):
    cart = Cart(request)
    product = get_object_or_404(MenuItem, id=item_id)
    # Get quantity from POST data, default to 1
    quantity = int(request.POST.get('quantity', 1))
    override_quantity = request.POST.get('override', False)
    
    cart.add(product=product, quantity=quantity, override_quantity=override_quantity)
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, item_id):
    cart = Cart(request)
    product = get_object_or_404(MenuItem, id=item_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})
