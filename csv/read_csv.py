import csv


valid_drivers = set()
with open("output/drivers.csv") as in_file:
    reader = csv.reader(in_file)
    next(reader)  # Skip header
    for line in reader:
        passed_theory = line[2]
        passed_practical = line[3]
        if passed_theory and passed_practical:
            valid_drivers.add(line[0])


print(valid_drivers)
