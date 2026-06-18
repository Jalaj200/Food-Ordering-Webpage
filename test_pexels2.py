import urllib.request, re, urllib.parse, json

queries = [
    'bacon mushroom pizza',
    'pad thai',
    'fish curry rice',
    'chole bhature',
    'tandoori chicken',
    'vegetable pulao',
    'aloo gobi',
    'garlic naan',
    'indian chicken curry',
    'apple crumble',
    'sticky toffee pudding',
    'avocado toast',
    'chicken wrap',
    'watermelon juice',
    'cold brew coffee',
    'sweet lassi',
    'iced matcha latte',
    'peach iced tea',
    'diet cola glass'
]

for q in queries:
    url = f'https://www.pexels.com/search/{urllib.parse.quote(q)}/'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/114.0.0.0 Safari/537.36'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        images = re.findall(r'src="(https://images\.pexels\.com/photos/[^"]+)"', html)
        if images:
            print(f"{q}: {images[0]}")
        else:
            print(f"{q}: NOT FOUND")
    except Exception as e:
        print(f"Error for {q}: {e}")
