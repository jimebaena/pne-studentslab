student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}

print("The student name is:", student["name"])
subjects = student["subjects"]
print("The number of subjects his enrolled:", len(subjects))
result = "PNE" in subjects
print("'PNE' is one of the subjects:", result)

grades = student["grades"]
print("Databases grade:", grades["Databases"])

total = 0
total_subjects = 0
for mark in grades.values():
    total += mark
    total_subjects += 1
print("The average grade is:", round(total / total_subjects, 2))