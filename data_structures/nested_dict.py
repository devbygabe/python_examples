rabbit = {
    "name": "Dexter",
    "breed": "Flemmish Giant",
    "owners": {
        "name": "Gabriel",
        "age": 32,
    },
}

# Print rabbit
print(rabbit)

# Get value from nested dict
owner_name = rabbit["owner"]["name"]
print(f"Rabbit owner: {owner_name}")
