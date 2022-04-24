fruits = ["Apple", "Orange", "Pear", "Apple"]

# Print fruits
print(fruits)

# Convert list to set
fruits_set = set(fruits)
print(f"Fruits as set: {fruits_set}")

# Convert back to unique list
unique_fruit_list = list(fruits_set)
print(f"Unique fruit list: {unique_fruit_list}")

# Make list unique (shorter)
unique_list = list(set(fruits))
print(f"Unique fruit list: {unique_list}")