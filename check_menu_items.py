import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_ordering.settings')
django.setup()

from menu.models import MenuItem

items = MenuItem.objects.all()
for item in items:
    print(f"ID: {item.id} | Name: {item.name} | Desc: {item.description} | Image: {item.image}")
