import json

car_str = {"make": "Tesla", "model": "Model Y"}
car = json.loads(car_str)

print(type(car))
print(car)

nums_str = "[1, 2, 3]"
nums = json.loads(nums_str)

print(type(nums))
print(nums)
