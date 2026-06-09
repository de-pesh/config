import requests
from bs4 import BeautifulSoup
import re
import json
import pandas as pd

# Step 1: Set the URL
url = 'https://www.carrefouruae.com/mafuae/en/c/NF4070900'  # Example site


# Step 1: Get the page
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

# Step 2: Parse the page
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find the <script> tag with JSON
script_tag = soup.find('script', text=re.compile(r'window\.__INITIAL_STATE__\s*='))

if not script_tag:
    print("Script tag with data not found")
    exit()

# Step 4: Extract JSON using regex
json_text_match = re.search(r'window\.__INITIAL_STATE__\s*=\s*(\[.*?\])\s*;', script_tag.string, re.DOTALL)

if not json_text_match:
    print("JSON data not found in script")
    exit()

json_text = json_text_match.group(1)

# Step 5: Parse JSON
data = json.loads(json_text)

# Step 6: Extract product data
products = []
for item in data:
    try:
        product = {
            'Name': item.get('name'),
            'Brand': item.get('brand', {}).get('name'),
            'Price': item.get('price', {}).get('price'),
            'Discounted Price': item.get('price', {}).get('discount', {}).get('price'),
            'Currency': item.get('price', {}).get('currency'),
            'Seller': item.get('supplier'),
        }
        products.append(product)
    except Exception as e:
        print("Error parsing product:", e)

# Step 7: Save to Excel
# df = pd.DataFrame(products)
# df.to_excel('products.xlsx', index=False)

# print("Saved to products.xlsx")
