import string

with open("alphabet.txt", "w") as out_file:
    out_file.write(string.ascii_lowercase)

print("Alphabet file created.")
