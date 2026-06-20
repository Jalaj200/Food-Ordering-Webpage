import os
import shutil
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_ordering.settings')
django.setup()

from menu.models import MenuItem

brain_dir = r"C:\Users\asus9\.gemini\antigravity-ide\brain\14b734b6-0a69-4f7b-84ac-c9e3f360c888"
media_dir = r"c:\Users\asus9\Desktop\Codes\Food_ordering\food_ordering\media\menu_images"

updates = [
    ("Double Cheese Bacon Burger", "double_cheese_bacon_burger_1781982328073.png", "double_cheese_bacon_burger.png"),
    ("Hawaiian Heat Wave", "hawaiian_heat_wave_1781982338816.png", "hawaiian_heat_wave.png"),
    ("Mediterranean Olive & Feta Pizza", "mediterranean_pizza_1781982350073.png", "mediterranean_olive_feta_pizza.png"),
    ("Rasmalai", "rasmalai_1781982361087.png", "rasmalai.png"),
    ("Seafood Marinara Spaghetti", "seafood_marinara_1781982371126.png", "seafood_marinara_spaghetti.png"),
    ("Garlic Butter Shrimp Pasta", "garlic_shrimp_pasta_1781982380802.png", "garlic_butter_shrimp_pasta.png"),
    ("Singapore Chili Rice Noodles", "singapore_noodles_1781982391416.png", "singapore_chili_rice_noodles.png"),
    ("Truffle Cream Gnocchi", "truffle_gnocchi_1781982402057.png", "truffle_cream_gnocchi.png"),
    ("Kesar Rasgulla", "kesar_rasgulla_1781982412846.png", "kesar_rasgulla.png"),
]

for item_name, src_name, dst_name in updates:
    src_path = os.path.join(brain_dir, src_name)
    dst_path = os.path.join(media_dir, dst_name)
    
    if os.path.exists(src_path):
        shutil.copy(src_path, dst_path)
        print(f"Copied {src_name} to {dst_name}")
    else:
        print(f"File not found: {src_path}")
        continue
        
    item = MenuItem.objects.filter(name=item_name).first()
    if item:
        item.image = f"menu_images/{dst_name}"
        item.save()
        print(f"Updated item {item.name}")
    else:
        print(f"Item {item_name} not found in DB")

