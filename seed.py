import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_ordering.settings')
django.setup()

from menu.models import Category, MenuItem


def seed():
    # Clear existing data for a fresh start
    MenuItem.objects.all().delete()
    Category.objects.all().delete()

    print("[*] Seeding food categories and items...\n")

    # ─────────────────────────────────────────────
    # Category 1: Burgers & Sandwiches
    # ─────────────────────────────────────────────
    cat_burgers = Category.objects.create(
        name='Burgers & Sandwiches',
        description='Juicy, flame-grilled burgers and handcrafted sandwiches piled high with fresh toppings.',
        icon='fa-burger',
    )
    burger_items = [
        {
            'name': 'Classic Smash Burger',
            'description': 'Double-smashed beef patties with melted American cheese, caramelized onions, pickles, and our signature Crave sauce on a toasted brioche bun.',
            'price': 299.00,
            'is_popular': True,
            'image': 'menu_images/classic_smash_burger.jpg',
        },
        {
            'name': 'Smoky BBQ Bacon Burger',
            'description': 'Chargrilled beef patty topped with crispy applewood smoked bacon, pepper jack cheese, crispy onion rings, and tangy BBQ glaze.',
            'price': 349.00,
            'is_popular': False,
            'image': 'menu_images/smoky_bbq_bacon_burger.jpg',
        },
        {
            'name': 'Spicy Chicken Burger',
            'description': 'Crispy buttermilk fried chicken breast tossed in fiery sriracha sauce, topped with coleslaw and jalapeño mayo on a sesame bun.',
            'price': 279.00,
            'is_popular': True,
            'image': 'menu_images/spicy_chicken_burger.jpg',
        },
        {
            'name': 'Mushroom Swiss Burger',
            'description': 'Juicy beef patty layered with sautéed wild mushrooms, melted Swiss cheese, garlic aioli, and fresh arugula.',
            'price': 329.00,
            'is_popular': False,
            'image': 'menu_images/mushroom_swiss_burger.jpg',
        },
        {
            'name': 'Paneer Tikka Burger',
            'description': 'Marinated paneer patty grilled to perfection with mint chutney, pickled onions, and crispy lettuce on a whole wheat bun.',
            'price': 229.00,
            'is_popular': False,
            'image': 'menu_images/paneer_tikka_burger.jpg',
        },
        {
            'name': 'Avocado Toast Club',
            'description': 'Freshly mashed seasoned avocado on toasted sourdough, layered with heirloom tomatoes, alfalfa sprouts, and cucumber ribbon salad.',
            'price': 249.00,
            'is_popular': False,
            'image': 'menu_images/avocado_toast_club.jpg',
        },
        {
            'name': 'Double Cheese Bacon Burger',
            'description': 'Two juicy beef patties loaded with double cheddar and Monterey Jack cheeses, crispy bacon, and sweet caramelized onion jam.',
            'price': 349.00,
            'is_popular': True,
            'image': 'menu_images/double_cheese_bacon_burger.jpg',
        },
        {
            'name': 'Crispy Fish Fillet Sandwich',
            'description': 'Golden-fried breaded sea bass fillet on a brioche bun with pickled cucumber tartar sauce and shredded iceberg lettuce.',
            'price': 299.00,
            'is_popular': False,
            'image': 'menu_images/crispy_fish_fillet_sandwich.jpg',
        },
        {
            'name': 'Pesto Caprese Panini',
            'description': 'Grilled panini filled with fresh mozzarella, sliced Roma tomatoes, nut-free basil pesto, and a drizzle of sweet balsamic reduction.',
            'price': 249.00,
            'is_popular': False,
            'image': 'menu_images/pesto_caprese_panini.jpg',
        },
        {
            'name': 'Tandoori Chicken Wrap',
            'description': 'Succulent clay-oven grilled chicken strips wrapped in a soft tortilla with mint mayonnaise, green peppers, and red onions.',
            'price': 229.00,
            'is_popular': False,
            'image': 'menu_images/tandoori_chicken_wrap.jpg',
        },
        {
            'name': 'Falafel Pita Pocket',
            'description': 'Crispy herb-infused chickpea falafels stuffed in a warm pita pocket with creamy hummus, tahini, and pickled garden vegetables.',
            'price': 199.00,
            'is_popular': False,
            'image': 'menu_images/falafel_pita_pocket.jpg',
        },
        {
            'name': 'BBQ Pulled Jackfruit Burger',
            'description': 'Slow-cooked hickory smoked pulled jackfruit piled high with tangy purple cabbage slaw on a toasted vegan potato bun.',
            'price': 249.00,
            'is_popular': False,
            'image': 'menu_images/bbq_pulled_jackfruit_burger.jpg',
        },
        {
            'name': 'Classic Club Sandwich',
            'description': 'A triple-decker sandwich loaded with grilled chicken breast, fried egg, crispy bacon, fresh lettuce, and tomatoes.',
            'price': 269.00,
            'is_popular': False,
            'image': 'menu_images/classic_club_sandwich.jpg',
        },
        {
            'name': 'Grilled Triple Cheese Melt',
            'description': 'A comforting blend of sharp cheddar, mozzarella, and Swiss cheeses melted between thick slices of butter-toasted brioche.',
            'price': 199.00,
            'is_popular': False,
            'image': 'menu_images/grilled_triple_cheese_melt.jpg',
        },
        {
            'name': 'Spicy Jalapeño Popper Burger',
            'description': 'Fire-grilled beef patty topped with deep-fried cream cheese jalapeño poppers, spicy salsa, and chipotle mayo.',
            'price': 329.00,
            'is_popular': False,
            'image': 'menu_images/spicy_jalapeno_popper_burger.jpg',
        },
    ]
    for item_data in burger_items:
        MenuItem.objects.create(category=cat_burgers, **item_data)
    print(f"  [+] {cat_burgers.name} -- {len(burger_items)} items")

    # ─────────────────────────────────────────────
    # Category 2: Pizzas
    # ─────────────────────────────────────────────
    cat_pizzas = Category.objects.create(
        name='Pizzas',
        description='Hand-tossed, stone-fired pizzas with artisanal toppings and our house-made tomato sauce.',
        icon='fa-pizza-slice',
    )
    pizza_items = [
        {
            'name': 'Margherita Classica',
            'description': 'San Marzano tomato sauce, fresh mozzarella di bufala, extra virgin olive oil, and fragrant basil leaves on a thin Neapolitan crust.',
            'price': 299.00,
            'is_popular': True,
            'image': 'menu_images/margherita_classica.jpg',
        },
        {
            'name': 'Pepperoni Supreme',
            'description': 'Loaded with spicy pepperoni, a blend of mozzarella and provolone cheeses, roasted garlic, and a drizzle of chili-infused honey.',
            'price': 399.00,
            'is_popular': True,
            'image': 'menu_images/pepperoni_supreme.jpg',
        },
        {
            'name': 'BBQ Chicken Ranch',
            'description': 'Smoky BBQ sauce base topped with grilled chicken, red onions, cilantro, smoked gouda, and a drizzle of ranch dressing.',
            'price': 449.00,
            'is_popular': False,
            'image': 'menu_images/bbq_chicken_ranch.jpg',
        },
        {
            'name': 'Veggie Garden Pizza',
            'description': 'A colorful medley of roasted bell peppers, sun-dried tomatoes, black olives, artichoke hearts, feta, and pesto drizzle.',
            'price': 349.00,
            'is_popular': False,
            'image': 'menu_images/veggie_garden_pizza.jpg',
        },
        {
            'name': 'Truffle Mushroom Pizza',
            'description': 'White truffle cream sauce with mixed wild mushrooms, caramelized onions, fontina cheese, and fresh thyme.',
            'price': 499.00,
            'is_popular': False,
            'image': 'menu_images/truffle_mushroom_pizza.jpg',
        },
        {
            'name': 'Four Cheese Bianca',
            'description': 'Creamy white sauce base topped with a decadent blend of mozzarella, gorgonzola, parmesan, and ricotta cheeses.',
            'price': 399.00,
            'is_popular': False,
            'image': 'menu_images/four_cheese_bianca.jpg',
        },
        {
            'name': 'Spicy Paneer Tikka Pizza',
            'description': 'Tandoori-spiced paneer cubes, red onions, and bell peppers topped with spicy green chili drizzle on stone-baked crust.',
            'price': 349.00,
            'is_popular': True,
            'image': 'menu_images/spicy_paneer_tikka_pizza.jpg',
        },
        {
            'name': 'Prosciutto & Arugula Pizza',
            'description': 'Thin crust Neapolitan pizza topped with aged prosciutto di Parma, fresh baby arugula, and shaved Parmigiano-Reggiano.',
            'price': 549.00,
            'is_popular': False,
            'image': 'menu_images/prosciutto_and_arugula_pizza.jpg',
        },
        {
            'name': 'Fiery Jalapeño & Pepper Pizza',
            'description': 'Spiced tomato base with red bell peppers, pickled jalapeños, red onions, and green chilies, finished with sriracha swirl.',
            'price': 349.00,
            'is_popular': False,
            'image': 'menu_images/fiery_jalapeno_and_pepper_pizza.jpg',
        },
        {
            'name': 'Hawaiian Heat Wave',
            'description': 'Sweet pineapple chunks, smoked ham slices, and pickled jalapeños on a classic marinara and mozzarella base.',
            'price': 399.00,
            'is_popular': False,
            'image': 'menu_images/hawaiian_heat_wave.jpg',
        },
        {
            'name': 'Chicken Tikka Masala Pizza',
            'description': 'Rich chicken tikka masala sauce, grilled chicken pieces, red onions, and fresh cilantro leaves on hand-tossed dough.',
            'price': 449.00,
            'is_popular': False,
            'image': 'menu_images/chicken_tikka_masala_pizza.jpg',
        },
        {
            'name': 'Garden Pesto Pizza',
            'description': 'House-made basil pesto base with cherry tomatoes, roasted garlic cloves, caramelized onions, and crumbled goat cheese.',
            'price': 349.00,
            'is_popular': False,
            'image': 'menu_images/garden_pesto_pizza.jpg',
        },
        {
            'name': 'Meat Lovers Feast',
            'description': 'A hearty combination of spicy pepperoni, seasoned Italian sausage, crispy bacon, and seasoned ground beef.',
            'price': 499.00,
            'is_popular': True,
            'image': 'menu_images/meat_lovers_feast.jpg',
        },
        {
            'name': 'Mediterranean Olive & Feta Pizza',
            'description': 'Sun-dried tomatoes, Kalamata olives, roasted artichoke hearts, and crumbled feta cheese with extra virgin olive oil.',
            'price': 349.00,
            'is_popular': False,
            'image': 'menu_images/mediterranean_olive_and_feta_pizza.jpg',
        },
        {
            'name': 'Smokey Bacon & Mushroom Pizza',
            'description': 'Garlic white sauce base topped with smoked bacon bits, sliced cremini mushrooms, caramelized onions, and fresh rosemary.',
            'price': 449.00,
            'is_popular': False,
            'image': 'menu_images/smokey_bacon_and_mushroom_pizza.jpg',
        },
    ]
    for item_data in pizza_items:
        MenuItem.objects.create(category=cat_pizzas, **item_data)
    print(f"  [+] {cat_pizzas.name} -- {len(pizza_items)} items")

    # ─────────────────────────────────────────────
    # Category 3: Indian Classics
    # ─────────────────────────────────────────────
    cat_indian = Category.objects.create(
        name='Indian Classics',
        description='Authentic Indian flavors — aromatic biryanis, rich curries, and freshly baked tandoor breads.',
        icon='fa-bowl-food',
    )
    indian_items = [
        {
            'name': 'Chicken Biryani',
            'description': 'Fragrant basmati rice layered with tender marinated chicken, saffron, fried onions, and traditional spices. Served with raita.',
            'price': 299.00,
            'is_popular': True,
            'image': 'menu_images/chicken_biryani.jpg',
        },
        {
            'name': 'Butter Chicken & Naan',
            'description': 'Succulent tandoori chicken pieces simmered in a velvety tomato-butter-cream gravy. Served with freshly baked garlic naan.',
            'price': 399.00,
            'is_popular': True,
            'image': 'menu_images/butter_chicken_and_naan.jpg',
        },
        {
            'name': 'Paneer Butter Masala',
            'description': 'Soft paneer cubes in a rich, creamy tomato-based gravy with kasuri methi and a touch of cream. A vegetarian favorite.',
            'price': 299.00,
            'is_popular': False,
            'image': 'menu_images/paneer_butter_masala.jpg',
        },
        {
            'name': 'Lamb Rogan Josh',
            'description': 'Slow-cooked lamb in a vibrant Kashmiri spice blend with yogurt, ginger, and whole aromatic spices.',
            'price': 449.00,
            'is_popular': False,
            'image': 'menu_images/lamb_rogan_josh.jpg',
        },
        {
            'name': 'Dal Makhani',
            'description': 'Black lentils and kidney beans slow-simmered overnight with butter, cream, and aromatic spices. Rich and comforting.',
            'price': 249.00,
            'is_popular': False,
            'image': 'menu_images/dal_makhani.jpg',
        },
        {
            'name': 'Goan Fish Curry & Rice',
            'description': 'Tender sea bass simmered in a spicy, tangy coconut-milk gravy with tamarind. Served with steamed basmati rice.',
            'price': 399.00,
            'is_popular': False,
            'image': 'menu_images/goan_fish_curry_and_rice.jpg',
        },
        {
            'name': 'Palak Paneer',
            'description': 'Fresh spinach puree cooked with cubes of paneer cheese, spiced with garlic, ginger, and cumin seeds.',
            'price': 279.00,
            'is_popular': False,
            'image': 'menu_images/palak_paneer.jpg',
        },
        {
            'name': 'Chole Bhature',
            'description': 'Spicy chickpeas cooked in a thick onion-tomato gravy, served with two fluffy deep-fried leavened bhaturas.',
            'price': 199.00,
            'is_popular': True,
            'image': 'menu_images/chole_bhature.jpg',
        },
        {
            'name': 'Mutton Seekh Kebab',
            'description': 'Minced lamb mixed with aromatic spices, skewered and grilled in the tandoor. Served with green mint chutney.',
            'price': 349.00,
            'is_popular': False,
            'image': 'menu_images/mutton_seekh_kebab.jpg',
        },
        {
            'name': 'Tandoori Chicken (Half)',
            'description': 'Chicken marinated in yogurt and tandoori spices, roasted in a clay oven. Served with sliced lemon and onions.',
            'price': 329.00,
            'is_popular': False,
            'image': 'menu_images/tandoori_chicken_half.jpg',
        },
        {
            'name': 'Malai Kofta',
            'description': 'Soft paneer and potato dumplings stuffed with dry fruits, simmered in a mild, creamy cashew gravy.',
            'price': 299.00,
            'is_popular': False,
            'image': 'menu_images/malai_kofta.jpg',
        },
        {
            'name': 'Vegetable Pulao',
            'description': 'Aromatic basmati rice cooked with mixed garden vegetables, cardamoms, cloves, and bay leaves.',
            'price': 229.00,
            'is_popular': False,
            'image': 'menu_images/vegetable_pulao.jpg',
        },
        {
            'name': 'Aloo Gobi Adraki',
            'description': 'A classic dry vegetarian dish featuring potatoes and cauliflower tossed with fresh ginger, cumin, and turmeric.',
            'price': 199.00,
            'is_popular': False,
            'image': 'menu_images/aloo_gobi_adraki.jpg',
        },
        {
            'name': 'Kadhai Chicken',
            'description': 'Chicken pieces cooked with bell peppers, tomatoes, and coarsely crushed coriander seeds in a traditional Kadhai wok.',
            'price': 359.00,
            'is_popular': False,
            'image': 'menu_images/kadhai_chicken.jpg',
        },
        {
            'name': 'Garlic Naan Basket',
            'description': 'A basket of three freshly baked garlic and butter naans from our tandoor clay oven. Perfect companion to curries.',
            'price': 99.00,
            'is_popular': False,
            'image': 'menu_images/garlic_naan_basket.jpg',
        },
    ]
    for item_data in indian_items:
        MenuItem.objects.create(category=cat_indian, **item_data)
    print(f"  [+] {cat_indian.name} -- {len(indian_items)} items")

    # ─────────────────────────────────────────────
    # Category 4: Pasta & Noodles
    # ─────────────────────────────────────────────
    cat_pasta = Category.objects.create(
        name='Pasta & Noodles',
        description='Italian pastas and Asian noodles — from creamy Alfredos to fiery stir-fries.',
        icon='fa-bowl-rice',
    )
    pasta_items = [
        {
            'name': 'Creamy Garlic Alfredo',
            'description': 'Fettuccine tossed in a luscious garlic Parmesan cream sauce with sautéed mushrooms and a touch of nutmeg.',
            'price': 299.00,
            'is_popular': True,
            'image': 'menu_images/creamy_garlic_alfredo.jpg',
        },
        {
            'name': 'Spicy Arrabbiata Penne',
            'description': 'Penne rigate in a fiery tomato sauce with red chili flakes, fresh garlic, basil, and shaved Pecorino Romano.',
            'price': 279.00,
            'is_popular': False,
            'image': 'menu_images/spicy_arrabbiata_penne.jpg',
        },
        {
            'name': 'Chicken Carbonara',
            'description': 'Spaghetti with crispy chicken bits, pancetta, egg yolk, Parmigiano-Reggiano, and cracked black pepper.',
            'price': 349.00,
            'is_popular': False,
            'image': 'menu_images/chicken_carbonara.jpg',
        },
        {
            'name': 'Hakka Noodles',
            'description': 'Wok-tossed noodles with julienned vegetables, soy sauce, chili vinegar, and a hint of sesame oil. Indo-Chinese style.',
            'price': 249.00,
            'is_popular': True,
            'image': 'menu_images/hakka_noodles.jpg',
        },
        {
            'name': 'Thai Basil Stir-Fry Noodles',
            'description': 'Wide rice noodles stir-fried with Thai basil, bell peppers, tofu, and a sweet-spicy soy sauce.',
            'price': 279.00,
            'is_popular': False,
            'image': 'menu_images/thai_basil_stir-fry_noodles.jpg',
        },
        {
            'name': 'Classic Lasagna Bolognese',
            'description': 'Layers of fresh pasta sheets, slow-simmered minced beef ragu, creamy béchamel, and melted mozzarella cheese.',
            'price': 349.00,
            'is_popular': True,
            'image': 'menu_images/classic_lasagna_bolognese.jpg',
        },
        {
            'name': 'Pesto Cavatappi',
            'description': 'Spiral pasta tossed in fresh basil-walnut pesto, cherry tomatoes, and baby spinach, finished with toasted pine nuts.',
            'price': 299.00,
            'is_popular': False,
            'image': 'menu_images/pesto_cavatappi.jpg',
        },
        {
            'name': 'Seafood Marinara Spaghetti',
            'description': 'Spaghetti pasta tossed with sautéed prawns, squid rings, and mussels in a garlic-herb marinara sauce.',
            'price': 449.00,
            'is_popular': False,
            'image': 'menu_images/seafood_marinara_spaghetti.jpg',
        },
        {
            'name': 'Singapore Chili Rice Noodles',
            'description': 'Thin vermicelli rice noodles wok-fried with curry powder, julienned peppers, cabbage, and egg.',
            'price': 249.00,
            'is_popular': False,
            'image': 'menu_images/singapore_chili_rice_noodles.jpg',
        },
        {
            'name': 'Four Cheese Mac & Cheese',
            'description': 'Elbow macaroni baked in a rich cheese sauce made from cheddar, gouda, mozzarella, and parmesan.',
            'price': 299.00,
            'is_popular': False,
            'image': 'menu_images/four_cheese_mac_and_cheese.jpg',
        },
        {
            'name': 'Truffle Cream Gnocchi',
            'description': 'Soft potato gnocchi tossed in a decadent black truffle cream sauce with wild mushrooms and fresh thyme.',
            'price': 399.00,
            'is_popular': False,
            'image': 'menu_images/truffle_cream_gnocchi.jpg',
        },
        {
            'name': 'Schezwan Egg Noodles',
            'description': 'Stir-fried Hakka noodles with scrambled egg, bell peppers, and scallions in a fiery Schezwan chili sauce.',
            'price': 249.00,
            'is_popular': False,
            'image': 'menu_images/schezwan_egg_noodles.jpg',
        },
        {
            'name': 'Spaghetti Bolognese',
            'description': 'Spaghetti served with a traditional slow-simmered ground beef and tomato ragout, finished with parmesan.',
            'price': 329.00,
            'is_popular': False,
            'image': 'menu_images/spaghetti_bolognese.jpg',
        },
        {
            'name': 'Vegetarian Pad Thai',
            'description': 'Flat rice noodles stir-fried in sweet-tangy tamarind sauce with tofu, bean sprouts, crushed peanuts, and chives.',
            'price': 259.00,
            'is_popular': False,
            'image': 'menu_images/vegetarian_pad_thai.jpg',
        },
        {
            'name': 'Garlic Butter Shrimp Pasta',
            'description': 'Linguine pasta tossed with succulent pan-seared shrimp in a rich garlic butter white wine sauce.',
            'price': 449.00,
            'is_popular': False,
            'image': 'menu_images/garlic_butter_shrimp_pasta.jpg',
        },
    ]
    for item_data in pasta_items:
        MenuItem.objects.create(category=cat_pasta, **item_data)
    print(f"  [+] {cat_pasta.name} -- {len(pasta_items)} items")

    # ─────────────────────────────────────────────
    # Category 5: Desserts & Sweets
    # ─────────────────────────────────────────────
    cat_desserts = Category.objects.create(
        name='Desserts & Sweets',
        description='Indulgent treats to end your meal on a sweet note — cakes, ice creams, and traditional delights.',
        icon='fa-ice-cream',
    )
    dessert_items = [
        {
            'name': 'Chocolate Lava Cake',
            'description': 'Warm dark chocolate cake with a molten gooey center, served with a scoop of vanilla bean ice cream and raspberry coulis.',
            'price': 199.00,
            'is_popular': True,
            'image': 'menu_images/chocolate_lava_cake.jpg',
        },
        {
            'name': 'Tiramisu',
            'description': 'Classic Italian dessert with espresso-soaked ladyfingers, mascarpone cream, and a dusting of cocoa powder.',
            'price': 249.00,
            'is_popular': False,
            'image': 'menu_images/tiramisu.jpg',
        },
        {
            'name': 'Gulab Jamun',
            'description': 'Soft, golden-fried milk dumplings soaked in warm rose-cardamom sugar syrup. Served 4 pieces per portion.',
            'price': 149.00,
            'is_popular': True,
            'image': 'menu_images/gulab_jamun.jpg',
        },
        {
            'name': 'New York Cheesecake',
            'description': 'Dense, creamy cheesecake on a buttery graham cracker crust topped with fresh mixed berry compote.',
            'price': 249.00,
            'is_popular': False,
            'image': 'menu_images/new_york_cheesecake.jpg',
        },
        {
            'name': 'Mango Kulfi',
            'description': 'Traditional Indian frozen dessert made with condensed milk, fresh Alphonso mango pulp, and crushed pistachios.',
            'price': 149.00,
            'is_popular': False,
            'image': 'menu_images/mango_kulfi.jpg',
        },
        {
            'name': 'Warm Apple Crumble',
            'description': 'Spiced apples baked under a crunchy cinnamon-oat streusel. Served warm with vanilla ice cream.',
            'price': 199.00,
            'is_popular': False,
            'image': 'menu_images/warm_apple_crumble.jpg',
        },
        {
            'name': 'Assorted Macarons (Box of 6)',
            'description': 'A selection of six colorful French macarons in pistachio, raspberry, chocolate, vanilla, salted caramel, and lemon.',
            'price': 349.00,
            'is_popular': True,
            'image': 'menu_images/assorted_macarons_box_of_6.jpg',
        },
        {
            'name': 'Double Chocolate Brownie',
            'description': 'Rich, fudgy chocolate brownie loaded with chocolate chunks, served warm with vanilla fudge drizzle.',
            'price': 179.00,
            'is_popular': False,
            'image': 'menu_images/double_chocolate_brownie.jpg',
        },
        {
            'name': 'Classic Crème Brûlée',
            'description': 'Creamy vanilla bean custard topped with a brittle layer of caramelized sugar.',
            'price': 249.00,
            'is_popular': False,
            'image': 'menu_images/classic_creme_brulee.jpg',
        },
        {
            'name': 'Rasmalai',
            'description': 'Flattened cottage cheese patties soaked in sweet, saffron-infused milk cream, garnished with pistachios.',
            'price': 179.00,
            'is_popular': False,
            'image': 'menu_images/rasmalai.jpg',
        },
        {
            'name': 'Red Velvet Cupcake',
            'description': 'Moist red velvet cake topped with a velvety, smooth cream cheese frosting swirl.',
            'price': 99.00,
            'is_popular': False,
            'image': 'menu_images/red_velvet_cupcake.jpg',
        },
        {
            'name': 'Sticky Toffee Pudding',
            'description': 'Classic British sponge cake made with finely chopped dates, covered in warm, rich toffee sauce.',
            'price': 219.00,
            'is_popular': False,
            'image': 'menu_images/sticky_toffee_pudding.jpg',
        },
        {
            'name': 'Mocha Mud Pie',
            'description': 'Coffee ice cream on a crunchy chocolate cookie crust, topped with dark chocolate hot fudge.',
            'price': 199.00,
            'is_popular': False,
            'image': 'menu_images/mocha_mud_pie.jpg',
        },
        {
            'name': 'Kesar Rasgulla',
            'description': 'Spongy chhena balls cooked in a light, sweet sugar syrup infused with pure Kashmiri saffron.',
            'price': 149.00,
            'is_popular': False,
            'image': 'menu_images/kesar_rasgulla.jpg',
        },
        {
            'name': 'Banana Split Sundae',
            'description': 'Three scoops of vanilla, chocolate, and strawberry ice cream nestled between a split banana with hot fudge.',
            'price': 249.00,
            'is_popular': False,
            'image': 'menu_images/banana_split_sundae.jpg',
        },
    ]
    for item_data in dessert_items:
        MenuItem.objects.create(category=cat_desserts, **item_data)
    print(f"  [+] {cat_desserts.name} -- {len(dessert_items)} items")

    # ─────────────────────────────────────────────
    # Category 6: Beverages
    # ─────────────────────────────────────────────
    cat_beverages = Category.objects.create(
        name='Beverages',
        description='Refreshing drinks to complement your meal — from freshly brewed coffees to tropical smoothies.',
        icon='fa-mug-hot',
    )
    beverage_items = [
        {
            'name': 'Iced Caramel Latte',
            'description': 'Double-shot espresso poured over ice with creamy milk and house-made caramel syrup. Topped with whipped cream.',
            'price': 179.00,
            'is_popular': True,
            'image': 'menu_images/iced_caramel_latte.jpg',
        },
        {
            'name': 'Mango Tango Smoothie',
            'description': 'A tropical blend of fresh Alphonso mango, banana, yogurt, and a splash of passion fruit juice.',
            'price': 149.00,
            'is_popular': True,
            'image': 'menu_images/mango_tango_smoothie.jpg',
        },
        {
            'name': 'Classic Masala Chai',
            'description': 'Strong Assam tea brewed with fresh ginger, cardamom, cinnamon, and cloves. Served with warm frothy milk.',
            'price': 79.00,
            'is_popular': False,
            'image': 'menu_images/classic_masala_chai.jpg',
        },
        {
            'name': 'Fresh Lime Soda',
            'description': 'Freshly squeezed lime juice with sparkling soda, a hint of rock salt, and mint leaves. Sweet or salted.',
            'price': 79.00,
            'is_popular': False,
            'image': 'menu_images/fresh_lime_soda.jpg',
        },
        {
            'name': 'Oreo Milkshake',
            'description': 'Thick and creamy vanilla milkshake blended with crushed Oreo cookies, topped with whipped cream and cookie crumbles.',
            'price': 199.00,
            'is_popular': False,
            'image': 'menu_images/oreo_milkshake.jpg',
        },
        {
            'name': 'Fresh Watermelon Juice',
            'description': 'Cold-pressed watermelon juice with a hint of fresh mint and black salt. Hydrating and refreshing.',
            'price': 99.00,
            'is_popular': False,
            'image': 'menu_images/fresh_watermelon_juice.jpg',
        },
        {
            'name': 'Double Espresso',
            'description': 'A bold, concentrated shot of double-espresso brewed from roasted premium Arabica beans.',
            'price': 99.00,
            'is_popular': False,
            'image': 'menu_images/double_espresso.jpg',
        },
        {
            'name': 'Cold Brew Coffee',
            'description': 'Steeped for 18 hours in cold filtered water, yielding a smooth, low-acid coffee served over ice.',
            'price': 149.00,
            'is_popular': False,
            'image': 'menu_images/cold_brew_coffee.jpg',
        },
        {
            'name': 'Classic Mojito',
            'description': 'Refreshing mocktail with muddled fresh mint leaves, lime wedges, organic sugar, and sparkling soda.',
            'price': 149.00,
            'is_popular': True,
            'image': 'menu_images/classic_mojito.jpg',
        },
        {
            'name': 'Strawberry Milkshake',
            'description': 'Creamy milkshake blended with sweet strawberries and vanilla ice cream, topped with strawberry syrup.',
            'price': 179.00,
            'is_popular': False,
            'image': 'menu_images/strawberry_milkshake.jpg',
        },
        {
            'name': 'Iced Matcha Green Tea',
            'description': 'Ceremonial grade Japanese matcha whisked with cold milk and lightly sweetened with honey.',
            'price': 179.00,
            'is_popular': False,
            'image': 'menu_images/iced_matcha_green_tea.jpg',
        },
        {
            'name': 'Sweet Lassi',
            'description': 'Traditional Punjabi sweet yogurt drink flavored with green cardamom and saffron rose water.',
            'price': 89.00,
            'is_popular': False,
            'image': 'menu_images/sweet_lassi.jpg',
        },
        {
            'name': 'Hot Cappuccino',
            'description': 'Espresso topped with equal parts steamed milk and rich, thick milk foam.',
            'price': 129.00,
            'is_popular': False,
            'image': 'menu_images/hot_cappuccino.jpg',
        },
        {
            'name': 'Sparkling Peach Iced Tea',
            'description': 'Brewed black tea infused with sweet peach syrup and soda, served ice-cold with fresh peach slices.',
            'price': 119.00,
            'is_popular': False,
            'image': 'menu_images/sparkling_peach_iced_tea.jpg',
        },
        {
            'name': 'Diet Cola',
            'description': 'Crisp, sugar-free carbonated soft drink served chilled with a fresh lemon wedge.',
            'price': 49.00,
            'is_popular': False,
            'image': 'menu_images/diet_cola.jpg',
        },
    ]
    for item_data in beverage_items:
        MenuItem.objects.create(category=cat_beverages, **item_data)
    print(f"  [+] {cat_beverages.name} -- {len(beverage_items)} items")

    total = MenuItem.objects.count()
    print(f"\n[OK] Done! Seeded {Category.objects.count()} categories with {total} total food items.")


if __name__ == '__main__':
    seed()
