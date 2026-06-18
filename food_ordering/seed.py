import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_ordering.settings')
django.setup()

from menu.models import Category, MenuItem

def seed():
    # Update older items to realistic INR prices
    MenuItem.objects.filter(name='Classic Cheeseburger').update(price=350.00)
    MenuItem.objects.filter(name='Pepperoni Pizza').update(price=550.00)
    MenuItem.objects.filter(name='Creamy Garlic Pasta').update(price=420.00)

    # Adding new Indian items
    cat4, _ = Category.objects.get_or_create(name='Indian Main Course')
    cat5, _ = Category.objects.get_or_create(name='Desserts')

    MenuItem.objects.get_or_create(
        name='Chicken Biryani',
        category=cat4,
        defaults={
            'description': 'A delicious plate of authentic Indian Chicken Biryani, garnished with fried onions.',
            'price': 480.00,
            'image': 'menu_images/biryani.png'
        }
    )

    MenuItem.objects.get_or_create(
        name='Butter Chicken & Naan',
        category=cat4,
        defaults={
            'description': 'A rich and creamy bowl of Butter Chicken accompanied by freshly baked naan bread.',
            'price': 520.00,
            'image': 'menu_images/butter_chicken.png'
        }
    )

    MenuItem.objects.get_or_create(
        name='Chocolate Fudge Dessert',
        category=cat5,
        defaults={
            'description': 'A decadent slice of dark chocolate fudge cake with a drizzle of chocolate sauce.',
            'price': 220.00,
            'image': 'menu_images/dessert.png'
        }
    )

    print("Database seeded with sample Indian items and updated prices.")

if __name__ == '__main__':
    seed()
