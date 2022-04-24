cart = [
    {"name": "Pencil"},
    {"name": "Paper"},
    {"name": "Stapler"},
]

try:
    item = cart[3]
    product = item["product"]
except IndexError:
    print("Not in cart.")
except KeyError:
    print("Product key not found.")
else:
    print(f"Product: {product}.")
finally:
    print("Finished checking.")
