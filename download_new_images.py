import os
import django
import urllib.request
import ssl

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_ordering.settings')
django.setup()

from django.conf import settings

media_dir = os.path.join(settings.MEDIA_ROOT, 'menu_images')
os.makedirs(media_dir, exist_ok=True)

IMAGE_URLS = {
    # Burgers & Sandwiches (10 items)
    'avocado_toast_club.jpg': 'https://images.unsplash.com/photo-1541532713592-79a0317b6b77?w=600&h=400&fit=crop',
    'double_cheese_bacon_burger.jpg': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600&h=400&fit=crop',
    'crispy_fish_fillet_sandwich.jpg': 'https://images.unsplash.com/photo-1534790566855-4cb788d389ec?w=600&h=400&fit=crop',
    'pesto_caprese_panini.jpg': 'https://images.unsplash.com/photo-1539252554453-80ab65ce3586?w=600&h=400&fit=crop',
    'tandoori_chicken_wrap.jpg': 'https://images.unsplash.com/photo-1617196034183-421b4917c92d?w=600&h=400&fit=crop',
    'falafel_pita_pocket.jpg': 'https://images.unsplash.com/photo-1598515214211-89d3c73ae83b?w=600&h=400&fit=crop',
    'bbq_pulled_jackfruit_burger.jpg': 'https://images.unsplash.com/photo-1525059696034-4967a8e1dca2?w=600&h=400&fit=crop',
    'classic_club_sandwich.jpg': 'https://images.unsplash.com/photo-1509722747041-616f39b57569?w=600&h=400&fit=crop',
    'grilled_triple_cheese_melt.jpg': 'https://images.unsplash.com/photo-1525351484163-7529414344d8?w=600&h=400&fit=crop',
    'spicy_jalapeno_popper_burger.jpg': 'https://images.unsplash.com/photo-1594212699903-ec8a3eca50f5?w=600&h=400&fit=crop',

    # Pizzas (10 items)
    'four_cheese_bianca.jpg': 'https://images.unsplash.com/photo-1573821663912-569905455b1c?w=600&h=400&fit=crop',
    'spicy_paneer_tikka_pizza.jpg': 'https://images.unsplash.com/photo-1593560708920-61dd98c46a4e?w=600&h=400&fit=crop',
    'prosciutto_and_arugula_pizza.jpg': 'https://images.unsplash.com/photo-1544982503-9f984c14501a?w=600&h=400&fit=crop',
    'fiery_jalapeno_and_pepper_pizza.jpg': 'https://images.unsplash.com/photo-1590947132387-155cc02f3212?w=600&h=400&fit=crop',
    'hawaiian_heat_wave.jpg': 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600&h=400&fit=crop',
    'chicken_tikka_masala_pizza.jpg': 'https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600&h=400&fit=crop',
    'garden_pesto_pizza.jpg': 'https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=600&h=400&fit=crop',
    'meat_lovers_feast.jpg': 'https://images.unsplash.com/photo-1534308983496-4fabb1a015ee?w=600&h=400&fit=crop',
    'mediterranean_olive_and_feta_pizza.jpg': 'https://images.unsplash.com/photo-1593560708920-61dd98c46a4e?w=600&h=400&fit=crop',
    'smokey_bacon_and_mushroom_pizza.jpg': 'https://images.unsplash.com/photo-1604917621956-10dfa7cce2e7?w=600&h=400&fit=crop',

    # Indian Classics (10 items)
    'goan_fish_curry_and_rice.jpg': 'https://images.unsplash.com/photo-1589301760014-d929f3979dbc?w=600&h=400&fit=crop',
    'palak_paneer.jpg': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=600&h=400&fit=crop',
    'chole_bhature.jpg': 'https://images.unsplash.com/photo-1626132647523-66f5bf380027?w=600&h=400&fit=crop',
    'mutton_seekh_kebab.jpg': 'https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?w=600&h=400&fit=crop',
    'tandoori_chicken_half.jpg': 'https://images.unsplash.com/photo-1626777552726-4a6b54c97e46?w=600&h=400&fit=crop',
    'malai_kofta.jpg': 'https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=600&h=400&fit=crop',
    'vegetable_pulao.jpg': 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=600&h=400&fit=crop',
    'aloo_gobi_adraki.jpg': 'https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=600&h=400&fit=crop',
    'kadhai_chicken.jpg': 'https://images.unsplash.com/photo-1626777552726-4a6b54c97e46?w=600&h=400&fit=crop',
    'garlic_naan_basket.jpg': 'https://images.unsplash.com/photo-1589301760014-d929f3979dbc?w=600&h=400&fit=crop',

    # Pasta & Noodles (10 items)
    'classic_lasagna_bolognese.jpg': 'https://images.unsplash.com/photo-1574894709920-11b28e7367e3?w=600&h=400&fit=crop',
    'pesto_cavatappi.jpg': 'https://images.unsplash.com/photo-1551183053-bf91a1d81141?w=600&h=400&fit=crop',
    'seafood_marinara_spaghetti.jpg': 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=600&h=400&fit=crop',
    'singapore_chili_rice_noodles.jpg': 'https://images.unsplash.com/photo-1585032226651-759b368d7246?w=600&h=400&fit=crop',
    'four_cheese_mac_and_cheese.jpg': 'https://images.unsplash.com/photo-1543339494-b4cd4f7ba686?w=600&h=400&fit=crop',
    'truffle_cream_gnocchi.jpg': 'https://images.unsplash.com/photo-1551183053-bf91a1d81141?w=600&h=400&fit=crop',
    'schezwan_egg_noodles.jpg': 'https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=600&h=400&fit=crop',
    'spaghetti_bolognese.jpg': 'https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?w=600&h=400&fit=crop',
    'vegetarian_pad_thai.jpg': 'https://images.unsplash.com/photo-1618083707368-b3823daa2726?w=600&h=400&fit=crop',
    'garlic_butter_shrimp_pasta.jpg': 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=600&h=400&fit=crop',

    # Desserts & Sweets (10 items)
    'warm_apple_crumble.jpg': 'https://images.unsplash.com/photo-1507226983735-a838615193b0?w=600&h=400&fit=crop',
    'assorted_macarons_box_of_6.jpg': 'https://images.unsplash.com/photo-1569864358642-9d1684040f43?w=600&h=400&fit=crop',
    'double_chocolate_brownie.jpg': 'https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=600&h=400&fit=crop',
    'classic_creme_brulee.jpg': 'https://images.unsplash.com/photo-1516685018646-549198525c1b?w=600&h=400&fit=crop',
    'rasmalai.jpg': 'https://images.unsplash.com/photo-1589301760014-d929f3979dbc?w=600&h=400&fit=crop',
    'red_velvet_cupcake.jpg': 'https://images.unsplash.com/photo-1576618148400-f54bed99fcfd?w=600&h=400&fit=crop',
    'sticky_toffee_pudding.jpg': 'https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=600&h=400&fit=crop',
    'mocha_mud_pie.jpg': 'https://images.unsplash.com/photo-1551024601-bec78aea704b?w=600&h=400&fit=crop',
    'kesar_rasgulla.jpg': 'https://images.unsplash.com/photo-1627308595229-7830a5c91f9f?w=600&h=400&fit=crop',
    'banana_split_sundae.jpg': 'https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=600&h=400&fit=crop',

    # Beverages (10 items)
    'fresh_watermelon_juice.jpg': 'https://images.unsplash.com/photo-1505253716362-afaea1d3d1af?w=600&h=400&fit=crop',
    'double_espresso.jpg': 'https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=600&h=400&fit=crop',
    'cold_brew_coffee.jpg': 'https://images.unsplash.com/photo-1517701604599-bb29b565090c?w=600&h=400&fit=crop',
    'classic_mojito.jpg': 'https://images.unsplash.com/photo-1536935338788-846bb9981813?w=600&h=400&fit=crop',
    'strawberry_milkshake.jpg': 'https://images.unsplash.com/photo-1579954115545-a95591f28bfc?w=600&h=400&fit=crop',
    'iced_matcha_green_tea.jpg': 'https://images.unsplash.com/photo-1536256263959-770b48d82b0a?w=600&h=400&fit=crop',
    'sweet_lassi.jpg': 'https://images.unsplash.com/photo-1553530666-ba11a7da3888?w=600&h=400&fit=crop',
    'hot_cappuccino.jpg': 'https://images.unsplash.com/photo-1534778101976-62847782c213?w=600&h=400&fit=crop',
    'sparkling_peach_iced_tea.jpg': 'https://images.unsplash.com/photo-1497515114629-f71d768fd07c?w=600&h=400&fit=crop',
    'diet_cola.jpg': 'https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=600&h=400&fit=crop',
}

# Allow unverified SSL for development
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

def download_images():
    success_count = 0
    fail_count = 0

    for filename, url in IMAGE_URLS.items():
        filepath = os.path.join(media_dir, filename)
        
        # Overwrite if file doesn't exist or is tiny placeholder
        if os.path.exists(filepath) and os.path.getsize(filepath) > 2000:
            # File already downloaded, skip
            success_count += 1
            continue

        print(f"  Downloading: {filename}...", end=' ')
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
            with urllib.request.urlopen(req, context=ssl_context, timeout=30) as response:
                with open(filepath, 'wb') as f:
                    f.write(response.read())
            print("OK")
            success_count += 1
        except Exception as e:
            print(f"FAILED ({e})")
            fail_count += 1

    print(f"\nDone! {success_count} images downloaded, {fail_count} failed.")

if __name__ == '__main__':
    print("[*] Downloading specific food images...\n")
    download_images()
