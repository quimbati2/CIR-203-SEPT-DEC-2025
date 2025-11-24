inventory = {
    "Laptop": 15,
    "Mouse": 50,
    "Keyboard": 25,
    "Monitor": 8,
    "Flash Drive": 5
}

inventory["Headphones"] = 30
inventory["Monitor"] = 12

def low_stock(inv):
    return [product for product, qty in inv.items() if qty < 10]

print(low_stock(inventory))

del inventory["Flash Drive"]
print(inventory)

for product, qty in inventory.items():
    print(product, qty)
