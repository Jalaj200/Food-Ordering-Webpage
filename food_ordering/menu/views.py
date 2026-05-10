from django.shortcuts import render
from .models import Category, MenuItem

def menu_list(request):
    categories = Category.objects.all()
    items = MenuItem.objects.filter(is_available=True)
    return render(request, 'menu/menu.html', {'categories': categories, 'items': items})
