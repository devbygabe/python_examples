import csv

total_stock = 0
with open("output/store.csv") as in_file:
    reader = csv.DictReader(in_file)
    for product in reader:
        quantity = int(product["Quantity"])
        total_stock += quantity

print(f"Total stock: {total_stock}")
