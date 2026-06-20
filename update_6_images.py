import os
import shutil
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_ordering.settings')
django.setup()

from menu.models import MenuItem

brain_dir = r"C:\Users\asus9\.gemini\antigravity-ide\brain\14b734b6-0a69-4f7b-84ac-c9e3f360c888"
media_dir = r"c:\Users\asus9\Desktop\Codes\Food_ordering\food_ordering\media\menu_images"

updates = [
    (295, "fresh_lime_soda_1781982079971.png", "fresh_lime_soda.png"),
    (279, "gulab_jamun_1781982098160.png", "gulab_jamun.png"),
    (291, "banana_split_1781982108944.png", "banana_split_sundae.png"),
    (273, "schezwan_noodles_1781982121557.png", "schezwan_egg_noodles.png"),
    (265, "hakka_noodles_1781982135837.png", "hakka_noodles.png"),
    (235, "veggie_pizza_1781982148919.png", "veggie_garden_pizza.png"),
]

for item_id, src_name, dst_name in updates:
    src_path = os.path.join(brain_dir, src_name)
    dst_path = os.path.join(media_dir, dst_name)
    
    # Copy file
    if os.path.exists(src_path):
        shutil.copy(src_path, dst_path)
        print(f"Copied {src_name} to {dst_name}")
    else:
        print(f"File not found: {src_path}")
        continue
        
    # Update DB
    try:
        item = MenuItem.objects.get(id=item_id)
        item.image = f"menu_images/{dst_name}"
        item.save()
        print(f"Updated item {item.name}")
    except MenuItem.DoesNotExist:
        print(f"Item ID {item_id} not found")

