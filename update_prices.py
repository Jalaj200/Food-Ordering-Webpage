import os
import django
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_ordering.settings')
django.setup()

from menu.models import MenuItem

price_map = {
    'Classic Smash Burger': 299.00,
    'Smoky BBQ Bacon Burger': 349.00,
    'Spicy Chicken Burger': 279.00,
    'Mushroom Swiss Burger': 329.00,
    'Paneer Tikka Burger': 229.00,
    'Avocado Toast Club': 249.00,
    'Double Cheese Bacon Burger': 349.00,
    'Crispy Fish Fillet Sandwich': 299.00,
    'Pesto Caprese Panini': 249.00,
    'Tandoori Chicken Wrap': 229.00,
    'Falafel Pita Pocket': 199.00,
    'BBQ Pulled Jackfruit Burger': 249.00,
    'Classic Club Sandwich': 269.00,
    'Grilled Triple Cheese Melt': 199.00,
    'Spicy Jalapeño Popper Burger': 329.00,
    'Margherita Classica': 299.00,
    'Pepperoni Supreme': 399.00,
    'BBQ Chicken Ranch': 449.00,
    'Veggie Garden Pizza': 349.00,
    'Truffle Mushroom Pizza': 499.00,
    'Four Cheese Bianca': 399.00,
    'Spicy Paneer Tikka Pizza': 349.00,
    'Prosciutto & Arugula Pizza': 549.00,
    'Fiery Jalapeño & Pepper Pizza': 349.00,
    'Hawaiian Heat Wave': 399.00,
    'Chicken Tikka Masala Pizza': 449.00,
    'Garden Pesto Pizza': 349.00,
    'Meat Lovers Feast': 499.00,
    'Mediterranean Olive & Feta Pizza': 349.00,
    'Smokey Bacon & Mushroom Pizza': 449.00,
    'Chicken Biryani': 299.00,
    'Butter Chicken & Naan': 399.00,
    'Paneer Butter Masala': 299.00,
    'Lamb Rogan Josh': 449.00,
    'Dal Makhani': 249.00,
    'Goan Fish Curry & Rice': 399.00,
    'Palak Paneer': 279.00,
    'Chole Bhature': 199.00,
    'Mutton Seekh Kebab': 349.00,
    'Tandoori Chicken (Half)': 329.00,
    'Malai Kofta': 299.00,
    'Vegetable Pulao': 229.00,
    'Aloo Gobi Adraki': 199.00,
    'Kadhai Chicken': 359.00,
    'Garlic Naan Basket': 99.00,
    'Creamy Garlic Alfredo': 299.00,
    'Spicy Arrabbiata Penne': 279.00,
    'Chicken Carbonara': 349.00,
    'Hakka Noodles': 249.00,
    'Thai Basil Stir-Fry Noodles': 279.00,
    'Classic Lasagna Bolognese': 349.00,
    'Pesto Cavatappi': 299.00,
    'Seafood Marinara Spaghetti': 449.00,
    'Singapore Chili Rice Noodles': 249.00,
    'Four Cheese Mac & Cheese': 299.00,
    'Truffle Cream Gnocchi': 399.00,
    'Schezwan Egg Noodles': 249.00,
    'Spaghetti Bolognese': 329.00,
    'Vegetarian Pad Thai': 259.00,
    'Garlic Butter Shrimp Pasta': 449.00,
    'Chocolate Lava Cake': 199.00,
    'Tiramisu': 249.00,
    'Gulab Jamun': 149.00,
    'New York Cheesecake': 249.00,
    'Mango Kulfi': 149.00,
    'Warm Apple Crumble': 199.00,
    'Assorted Macarons (Box of 6)': 349.00,
    'Double Chocolate Brownie': 179.00,
    'Classic Crème Brûlée': 249.00,
    'Rasmalai': 179.00,
    'Red Velvet Cupcake': 99.00,
    'Sticky Toffee Pudding': 219.00,
    'Mocha Mud Pie': 199.00,
    'Kesar Rasgulla': 149.00,
    'Banana Split Sundae': 249.00,
    'Iced Caramel Latte': 179.00,
    'Mango Tango Smoothie': 149.00,
    'Classic Masala Chai': 79.00,
    'Fresh Lime Soda': 79.00,
    'Oreo Milkshake': 199.00,
    'Fresh Watermelon Juice': 99.00,
    'Double Espresso': 99.00,
    'Cold Brew Coffee': 149.00,
    'Classic Mojito': 149.00,
    'Strawberry Milkshake': 179.00,
    'Iced Matcha Green Tea': 179.00,
    'Sweet Lassi': 89.00,
    'Hot Cappuccino': 129.00,
    'Sparkling Peach Iced Tea': 119.00,
    'Diet Cola': 49.00
}

# 1. Update Database
count = 0
for name, new_price in price_map.items():
    item = MenuItem.objects.filter(name=name).first()
    if item:
        item.price = new_price
        item.save()
        count += 1
print(f'Updated {count} items in database.')

# 2. Update seed.py
with open('seed.py', 'r', encoding='utf-8') as f:
    seed_content = f.read()

def update_seed_price(match):
    name = match.group(1)
    if name in price_map:
        return f"'name': '{name}',\n            'description':{match.group(2)}\n            'price': {price_map[name]:.2f},"
    return match.group(0)

# The pattern looks for 'name': 'Item Name',\n            'description': '...',\n            'price': XXX.XX,
new_seed_content = re.sub(
    r"'name':\s*'([^']*)',\s*\n\s*'description':(.*?)\n\s*'price':\s*[\d\.]+,",
    update_seed_price,
    seed_content,
    flags=re.DOTALL
)

with open('seed.py', 'w', encoding='utf-8') as f:
    f.write(new_seed_content)

print('Updated seed.py.')
