import os
import django
import urllib.request
import json
import ssl

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_ordering.settings')
django.setup()

from menu.models import MenuItem
from django.conf import settings

media_dir = os.path.join(settings.MEDIA_ROOT, 'menu_images')

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

FIX_MAP = {
    'Double Cheese Bacon Burger': 'Bacon Cheeseburger',
    'Hawaiian Heat Wave': 'Hawaiian Pizza',
    'Mediterranean Olive & Feta Pizza': 'Olive Pizza',
    'Vegetable Pulao': 'Vegetable Pulao',
    'Garlic Naan Basket': 'Garlic Naan',
    'Rasmalai': 'Ras malai',
    'Kadhai Chicken': 'Chicken Karahi',
    'Seafood Marinara Spaghetti': 'Spaghetti marinara',
    'Garlic Butter Shrimp Pasta': 'Shrimp pasta',
    'Singapore Chili Rice Noodles': 'Singapore noodles',
    'Truffle Cream Gnocchi': 'Gnocchi',
    'Kesar Rasgulla': 'Rasgulla',
    'Cold Brew Coffee': 'Cold Brew Coffee',
    'Sticky Toffee Pudding': 'Sticky Toffee Pudding',
    'Diet Cola': 'Diet Coke glass'
}

def search_wikimedia(query):
    url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=pageimages&generator=search&gsrsearch={urllib.parse.quote(query)}&gsrlimit=3&pithumbsize=600"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        resp = urllib.request.urlopen(req, context=ssl_context).read().decode('utf-8')
        data = json.loads(resp)
        pages = data.get('query', {}).get('pages', {})
        for p in pages.values():
            if 'thumbnail' in p:
                return p['thumbnail']['source']
    except Exception as e:
        print(f"Error searching {query}: {e}")
    return None

def main():
    success = 0
    for item_name, search_term in FIX_MAP.items():
        item = MenuItem.objects.filter(name=item_name).first()
        if not item:
            print(f"Item not found: {item_name}")
            continue
            
        img_url = search_wikimedia(search_term)
        if not img_url:
            # Fallback search
            img_url = search_wikimedia(item_name)
            
        if img_url:
            filename = item.name.lower().replace(' ', '_').replace('&', 'and').replace("'", "") + "_fixed.jpg"
            filepath = os.path.join(media_dir, filename)
            
            print(f"Downloading {item_name} from {img_url}...")
            try:
                req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, context=ssl_context, timeout=15) as response:
                    with open(filepath, 'wb') as f:
                        f.write(response.read())
                
                item.image = f"menu_images/{filename}"
                item.save()
                success += 1
                print(f"  OK")
            except Exception as e:
                print(f"  Failed: {e}")
        else:
            print(f"No image found for {item_name}")
            
    print(f"\nSuccessfully fixed {success}/{len(FIX_MAP)} images.")

if __name__ == '__main__':
    main()
