names = ["Leto", "Indy", "Finn"]

# Update name by index
names[1] = "Chloe"

# Append name
names.append("Indy")

# Extend list with 3 more items
names.extend(["Leo", "Dexter", "Ellie"])

# Remove name from list
names.remove("Indy")

# Remove first name from list and return
removed_name = names.pop()
print(f"Removed: {removed_name}")

# Print names list
print(names)

# Print name at specific index
print(names[2])

# Check if name IS in list
if "Finn" in names:
    print("Finn is in names.")

# Check if name NOT in list
if "Fido" not in names:
    print("Fido is not in names.")
