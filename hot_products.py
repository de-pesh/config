# from bs4 import BeautifulSoup
# from lxml import html
# import requests

# page = requests.get('https://www.carrefouruae.com/mafuae/en/c/NF4070900')

import requests
import re
import html
import pandas as pd

# Step 1: Get the page content
url = 'https://www.carrefouruae.com/mafuae/en/c/NF4070900'  # Replace with actual URL


# Step 1: Request the page
# url = 'https://your_url_here.com'  # Replace with actual URL
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

# Step 2: Decode the content
data = response.content.decode('utf-8')

# Step 3: Extract product name and price using regex
pattern = r'"name":"(.*?)".*?"price":\{"currency":".*?","price":(.*?)[,}]'

matches = re.findall(pattern, data, re.DOTALL)

# Step 4: Clean and save
products = []
for name, price in matches:
    try:
        clean_name = html.unescape(name)
        clean_price = float(price)
        products.append({'Name': clean_name, 'Price': clean_price})
    except:
        continue
print(products)
# # Step 5: Save to Excel
# df = pd.DataFrame(products)
# df.to_excel('products.xlsx', index=False)

# print(f"✅ Done. Extracted {len(products)} products.")
