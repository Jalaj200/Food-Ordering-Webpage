import urllib.request, json, urllib.parse

queries = {
    'Smokey Bacon & Mushroom Pizza': 'Pizza mushroom bacon',
    'Vegetarian Pad Thai': 'Pad Thai vegetarian',
    'Goan Fish Curry & Rice': 'Goan fish curry',
    'Chole Bhature': 'Chole bhature',
    'Tandoori Chicken (Half)': 'Tandoori chicken',
    'Vegetable Pulao': 'Vegetable Pulao',
    'Aloo Gobi Adraki': 'Aloo Gobi',
    'Garlic Naan Basket': 'Garlic Naan',
    'Kadhai Chicken': 'Chicken Karahi',
    'Warm Apple Crumble': 'Apple crumble',
    'Sticky Toffee Pudding': 'Sticky toffee pudding',
    'Avocado Toast Club': 'Avocado toast sandwich',
    'Tandoori Chicken Wrap': 'Chicken wrap',
    'Fresh Watermelon Juice': 'Watermelon juice',
    'Cold Brew Coffee': 'Cold brew coffee glass',
    'Sweet Lassi': 'Lassi drink',
    'Iced Matcha Green Tea': 'Iced matcha latte',
    'Sparkling Peach Iced Tea': 'Peach iced tea',
    'Diet Cola': 'Diet Coke glass'
}

for name, q in queries.items():
    url = f'https://en.wikipedia.org/w/api.php?action=query&format=json&prop=pageimages&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrlimit=3&pithumbsize=600'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 FoodApp/1.0'})
    print(f'\n=== {name} ===')
    try:
        resp = urllib.request.urlopen(req).read().decode('utf-8')
        pages = json.loads(resp).get('query', {}).get('pages', {})
        for p in pages.values():
            if 'thumbnail' in p:
                print(f"{p.get('title')}: {p['thumbnail']['source']}")
    except Exception as e:
        print(f"Error: {e}")
