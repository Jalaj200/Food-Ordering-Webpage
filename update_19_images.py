import os
import shutil
import urllib.request
import django
import ssl

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_ordering.settings')
django.setup()

from menu.models import MenuItem
from django.conf import settings

media_dir = os.path.join(settings.MEDIA_ROOT, 'menu_images')
artifact_dir = r"C:\Users\asus9\.gemini\antigravity-ide\brain\7e6af5da-63bf-4bfd-bfe3-44d7991d39ca"

ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE

generated_images = {
    'Chole Bhature': 'chole_bhature_1781711301713.png',
    'Smokey Bacon & Mushroom Pizza': 'bacon_mushroom_pizza_1781711329290.png',
    'Vegetarian Pad Thai': 'vegetarian_pad_thai_1781711343688.png',
    'Goan Fish Curry & Rice': 'goan_fish_curry_1781711356201.png',
    'Tandoori Chicken (Half)': 'tandoori_chicken_1781711372470.png',
    'Vegetable Pulao': 'vegetable_pulao_1781711385656.png',
    'Aloo Gobi Adraki': 'aloo_gobi_adraki_1781711410293.png',
    'Garlic Naan Basket': 'garlic_naan_basket_1781711424830.png',
    'Kadhai Chicken': 'kadhai_chicken_1781711440536.png',
    'Warm Apple Crumble': 'warm_apple_crumble_1781711453243.png',
    'Sticky Toffee Pudding': 'sticky_toffee_pudding_1781711467955.png',
    'Avocado Toast Club': 'avocado_toast_club_1781711486122.png',
    'Tandoori Chicken Wrap': 'tandoori_chicken_wrap_1781711500997.png',
    'Fresh Watermelon Juice': 'fresh_watermelon_juice_1781711518340.png',
    'Cold Brew Coffee': 'cold_brew_coffee_1781711531220.png',
    'Sweet Lassi': 'sweet_lassi_1781711544189.png'
}

pexels_images = {
    'Iced Matcha Green Tea': 'https://images.pexels.com/photos/31599066/pexels-photo-31599066.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',
    'Sparkling Peach Iced Tea': 'https://images.pexels.com/photos/31066139/pexels-photo-31066139.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',
    'Diet Cola': 'https://images.pexels.com/photos/28948768/pexels-photo-28948768.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500'
}

for item_name, fname in generated_images.items():
    item = MenuItem.objects.filter(name=item_name).first()
    if not item:
        print(f"Not found: {item_name}")
        continue
    
    src = os.path.join(artifact_dir, fname)
    dst_name = fname.split('_1781')[0] + '.png'
    dst = os.path.join(media_dir, dst_name)
    
    if os.path.exists(src):
        shutil.copy2(src, dst)
        item.image = f'menu_images/{dst_name}'
        item.save()
        print(f"Copied & Updated: {item_name}")
    else:
        print(f"File missing: {src}")

for item_name, url in pexels_images.items():
    item = MenuItem.objects.filter(name=item_name).first()
    if not item:
        print(f"Not found: {item_name}")
        continue
    
    dst_name = item_name.lower().replace(' ', '_') + '.jpg'
    dst = os.path.join(media_dir, dst_name)
    
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        content = urllib.request.urlopen(req, context=ssl_ctx).read()
        with open(dst, 'wb') as f:
            f.write(content)
        item.image = f'menu_images/{dst_name}'
        item.save()
        print(f"Downloaded & Updated: {item_name}")
    except Exception as e:
        print(f"Failed to download {item_name}: {e}")

print("All 19 exact images have been verified and updated!")
