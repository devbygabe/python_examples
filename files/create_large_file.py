with open("nums.txt", "w") as out_file:
    for i in range(1, 1000001):
        out_file.write(f"{i}\n")

print("Finished creating large file.")
