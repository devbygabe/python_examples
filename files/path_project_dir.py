import os

# Build path
base_dir = os.getcwd()
sub_dir = "output"
full_dir_path = os.path.join(base_dir, sub_dir)

# Create dir
os.makedirs(full_dir_path, exist_ok=True)

# Write content to file in created dir
file_path = os.path.join(full_dir_path, "message.txt")
with open(file_path, "a") as out_file:
    out_file.write("Hello!\n")
