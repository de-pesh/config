import json

FILE = "my_app_venv\\products.json"

def load_data(filename= FILE):
    with open(filename, "r") as f:
        return json.load(f)

def save_data(data, filename=FILE):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)


def create_product(product, filename=FILE):
    data = load_data(filename)
    data.append(product)
    save_data(data, filename)


def read_product(product_link, filename=FILE):
    data = load_data(filename)
    for product in data:
        if product["product_link"] == product_link:
            return product
    return None


def update_product(product_link, updates, filename=FILE):
    data = load_data(filename)
    for product in data:
        if product["product_link"] == product_link:
            product.update(updates)
            save_data(data, filename)
            return True
    return False


def delete_product(product_link, filename=FILE):
    data = load_data(filename)
    new_data = [p for p in data if p["product_link"] != product_link]
    if len(new_data) == len(data):
        return False  # Product not found
    save_data(new_data, filename)
    return True

def read_all_products(filename=FILE):
    with open(filename, "r") as f:
        return json.load(f)

print(read_all_products())