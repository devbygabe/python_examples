student_count = {
    "course_1": 923,
    "course_2": 7738,
    "course_3": 112,
}

# Loop through items in dictionary
for key, value in student_count.items():
    print(f"{key}: {value}")

# Count the total number of students
total_students = 0
for key, value in student_count.items():
    total_students += value

print(f"Total students: {total_students}")

# get all keys from dictionary
courses = student_count.keys()
print(courses)
