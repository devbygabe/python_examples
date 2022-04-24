import json

with open("output.user.json") as in_file:
    user = json.load(in_file)


print(type(user))
print(user)


fav_nums = user["fav_nums"]
print(type(fav_nums))
print(fav_nums)
