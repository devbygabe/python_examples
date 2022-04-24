rabbit = {"name": "Dexter", "breed": "Flemmish Giant", "Colour": "Fawn"}

# Print rabbit
print(rabbit)

# Add age to rabbit
rabbit["age"] = 3
print(rabbit)

# Remove from rabbit
age = rabbit.pop("age")
print(f"Removed age: {age}")
print(rabbit)

# Get name from rabbit
name = rabbit.get("name")
print("Rabbit name: {name}")

# Get name from rabbit with default
name = rabbit.get("name1", "name1 not set")
print("Rabbit name: {name}")

# Clear rabbit
rabbit.clear()
print(rabbit)
