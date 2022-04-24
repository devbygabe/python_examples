import os
import csv

current_dir = os.getcwd()
output_dir_path = os.path.join(current_dir, "output")
os.makedirs(output_dir_path, exist_ok=True)
csv_file_path = os.path.join(output_dir_path, "drivers.csv")

with open(csv_file_path, "w", newline="") as out_file:
    writer = csv.writer(out_file)
    writer.writerow(["Jame", 34, True, True])
