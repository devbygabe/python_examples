with open("Alphabet.txt") as in_file:
    print(f"Location when opening: {in_file.tell()}")
    print(f"Letter letter: {in_file.read(1)}")
    print(f"Second letter letter: {in_file.read(1)}")
    in_file.seek(4)
    print(f"Fifth letter letter: {in_file.read(1)}")
