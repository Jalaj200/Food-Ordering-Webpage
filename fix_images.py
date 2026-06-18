"""Fix the 4 failed image downloads with alternate URLs."""
import os
import django
import urllib.request
import ssl

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_ordering.settings')
django.setup()

from menu.models import MenuItem
from django.conf import settings

media_dir = os.path.join(settings.MEDIA_ROOT, 'menu_images')

FIXES = {
    'Thai Basil Stir-Fry Noodles': 'https://images.unsplash.com/photo-1585032226651-759b368d7246?w=600&h=400&fit=crop',
    'Gulab Jamun': 'https://images.unsplash.com/photo-1627308595229-7830a5c91f9f?w=600&h=400&fit=crop',
    'New York Cheesecake': 'https://images.unsplash.com/photo-1533134242443-d4fd215305ad?w=600&h=400&fit=crop',
    'Fresh Lime Soda': 'https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=600&h=400&fit=crop',
}

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

for name, url in FIXES.items():
    item = MenuItem.objects.filter(name=name).first()
    if not item:
        print(f"  Item not found: {name}")
        continue

    filename = name.lower().replace(' ', '_').replace('&', 'and').replace("'", '') + '.jpg'
    filepath = os.path.join(media_dir, filename)

    print(f"  Downloading: {name}...", end=' ')
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        with urllib.request.urlopen(req, context=ssl_context, timeout=30) as response:
            with open(filepath, 'wb') as f:
                f.write(response.read())
        item.image = f'menu_images/{filename}'
        item.save()
        print("OK")
    except Exception as e:
        print(f"FAILED ({e})")

print("\nDone fixing images.")
