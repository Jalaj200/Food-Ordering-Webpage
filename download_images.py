"""
Download food images from free image sources and assign them to menu items.
Uses picsum/placeholder approach with food-specific images from Unsplash source.
"""
import os
import django
import urllib.request
import ssl

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_ordering.settings')
django.setup()

from menu.models import MenuItem
from django.conf import settings

# Create media directory if it doesn't exist
media_dir = os.path.join(settings.MEDIA_ROOT, 'menu_images')
os.makedirs(media_dir, exist_ok=True)

# Map each food item to a relevant Unsplash image search
# Using source.unsplash.com for free, high-quality food images
IMAGE_URLS = {
    # Burgers & Sandwiches
    'Classic Smash Burger': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600&h=400&fit=crop',
    'Smoky BBQ Bacon Burger': 'https://images.unsplash.com/photo-1553979459-d2229ba7433b?w=600&h=400&fit=crop',
    'Spicy Chicken Burger': 'https://images.unsplash.com/photo-1606755962773-d324e0a13086?w=600&h=400&fit=crop',
    'Mushroom Swiss Burger': 'https://images.unsplash.com/photo-1572802419224-296b0aeee0d9?w=600&h=400&fit=crop',
    'Paneer Tikka Burger': 'https://images.unsplash.com/photo-1585238341710-4d3ff484184d?w=600&h=400&fit=crop',

    # Pizzas
    'Margherita Classica': 'https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=600&h=400&fit=crop',
    'Pepperoni Supreme': 'https://images.unsplash.com/photo-1628840042765-356cda07504e?w=600&h=400&fit=crop',
    'BBQ Chicken Ranch': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600&h=400&fit=crop',
    'Veggie Garden Pizza': 'https://images.unsplash.com/photo-1511689660979-10d2b1aada49?w=600&h=400&fit=crop',
    'Truffle Mushroom Pizza': 'https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600&h=400&fit=crop',

    # Indian Classics
    'Chicken Biryani': 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=600&h=400&fit=crop',
    'Butter Chicken & Naan': 'https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=600&h=400&fit=crop',
    'Paneer Butter Masala': 'https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=600&h=400&fit=crop',
    'Lamb Rogan Josh': 'https://images.unsplash.com/photo-1545247181-516773cae754?w=600&h=400&fit=crop',
    'Dal Makhani': 'https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=600&h=400&fit=crop',

    # Pasta & Noodles
    'Creamy Garlic Alfredo': 'https://images.unsplash.com/photo-1645112411341-6c4fd023714a?w=600&h=400&fit=crop',
    'Spicy Arrabbiata Penne': 'https://images.unsplash.com/photo-1563379926898-05f4575a45d8?w=600&h=400&fit=crop',
    'Chicken Carbonara': 'https://images.unsplash.com/photo-1612874742237-6526221588e3?w=600&h=400&fit=crop',
    'Hakka Noodles': 'https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=600&h=400&fit=crop',
    'Thai Basil Stir-Fry Noodles': 'https://images.unsplash.com/photo-1552611052-33e04de1b100?w=600&h=400&fit=crop',

    # Desserts & Sweets
    'Chocolate Lava Cake': 'https://images.unsplash.com/photo-1624353365286-3f8d62daad51?w=600&h=400&fit=crop',
    'Tiramisu': 'https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=600&h=400&fit=crop',
    'Gulab Jamun': 'https://images.unsplash.com/photo-1666190020613-1dcfaf1c8563?w=600&h=400&fit=crop',
    'New York Cheesecake': 'https://images.unsplash.com/photo-1524351199432-d330df18e1cd?w=600&h=400&fit=crop',
    'Mango Kulfi': 'https://images.unsplash.com/photo-1488900128323-21503983a07e?w=600&h=400&fit=crop',

    # Beverages
    'Iced Caramel Latte': 'https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=600&h=400&fit=crop',
    'Mango Tango Smoothie': 'https://images.unsplash.com/photo-1623065422902-30a2d299bbe4?w=600&h=400&fit=crop',
    'Classic Masala Chai': 'https://images.unsplash.com/photo-1597318181409-cf64d0b5d8a2?w=600&h=400&fit=crop',
    'Fresh Lime Soda': 'https://images.unsplash.com/photo-1513558161293-cdaf765ed514?w=600&h=400&fit=crop',
    'Oreo Milkshake': 'https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=600&h=400&fit=crop',
}

# Allow unverified SSL for development
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE


def download_images():
    items = MenuItem.objects.all()
    success_count = 0
    fail_count = 0

    for item in items:
        if item.name in IMAGE_URLS:
            url = IMAGE_URLS[item.name]
            # Create a safe filename
            filename = item.name.lower().replace(' ', '_').replace('&', 'and').replace("'", '') + '.jpg'
            filepath = os.path.join(media_dir, filename)

            print(f"  Downloading: {item.name}...", end=' ')
            try:
                req = urllib.request.Request(url, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                })
                with urllib.request.urlopen(req, context=ssl_context, timeout=30) as response:
                    with open(filepath, 'wb') as f:
                        f.write(response.read())

                # Update the model
                item.image = f'menu_images/{filename}'
                item.save()
                print("OK")
                success_count += 1

            except Exception as e:
                print(f"FAILED ({e})")
                fail_count += 1
        else:
            print(f"  Skipping: {item.name} (no URL mapped)")

    print(f"\nDone! {success_count} images downloaded, {fail_count} failed.")


if __name__ == '__main__':
    print("[*] Downloading food images...\n")
    download_images()
