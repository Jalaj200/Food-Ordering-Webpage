import urllib.request, re, urllib.parse, json

queries = ['pad thai', 'chole bhature']
for q in queries:
    url = f'https://www.pexels.com/search/{urllib.parse.quote(q)}/'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/114.0.0.0 Safari/537.36'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        images = re.findall(r'src="(https://images\.pexels\.com/photos/[^"]+)"', html)
        print(f"{q}: {list(set(images))[:3]}")
    except Exception as e:
        print(f"Error for {q}: {e}")
