products = []

def add_product(name, price):
    products.append({"name": name, "price": price})

def list_products():
    for i, p in enumerate(products, 1):
        print(f"{i}. {p['name']} - ${p['price']}")

if __name__ == "__main__":
    add_product("Laptop", 999)
    add_product("Mouse", 25)
    list_products()
