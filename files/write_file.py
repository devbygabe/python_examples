file_path = "out.txt"


# Single line
# text_line = "This is a line!\n"
# with open(file_path, "w") as out_file:
#     out_file.write(text_line)


# Multiple lines
text_lines = ["Line 01!\n", "line 03!\n", "line 03!\n"]
with open(file_path, "w") as out_file:
    out_file.writelines(text_lines)
