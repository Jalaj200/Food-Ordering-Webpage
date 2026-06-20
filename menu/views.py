from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Category, MenuItem


def menu_list(request):
    categories = Category.objects.prefetch_related('items').all()
    selected_category = request.GET.get('category', None)
    search_query = request.GET.get('search', '').strip()

    items = MenuItem.objects.filter(is_available=True)
    all_items_count = items.count()

    if selected_category:
        items = items.filter(category__slug=selected_category)
    
    if search_query:
        items = items.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(category__name__icontains=search_query)
        )

    return render(request, 'menu/menu.html', {
        'categories': categories,
        'items': items.select_related('category').distinct(),
        'selected_category': selected_category,
        'search_query': search_query,
        'all_items_count': all_items_count,
    })


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    items = MenuItem.objects.filter(category=category, is_available=True)
    categories = Category.objects.all()
    return render(request, 'menu/category_detail.html', {
        'category': category,
        'items': items,
        'categories': categories,
    })

def offers(request):
    return render(request, 'offers.html')

from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # Here we would normally save to DB or send email
        messages.success(request, 'Thank you for contacting us! We will get back to you shortly.')
    return render(request, 'contact.html')
