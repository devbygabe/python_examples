course_a = {"James", "Brooke", "Kath", "Mark", "Peter", "Anand"}
course_b = {"Sudie", "Suresh", "Simon", "Peter", "Greg", "Kath"}

# Students who took both course (intersection)
intersect = course_a & course_b
print(f"Took both course: {intersect}")

# Students from both courses combined (union)
union = course_a | course_b
print(f"All students: {union}")

# Students who only took one course (symmetric_difference)
sym_diff = course_a ^ course_b
print(f"Took one course: {sym_diff}")
