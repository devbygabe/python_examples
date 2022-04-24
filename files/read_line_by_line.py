sum_of_nums = 0

with open("nums.txt") as in_file:
    for line in in_file:
        sum_of_nums += int(line)

print(sum_of_nums)
