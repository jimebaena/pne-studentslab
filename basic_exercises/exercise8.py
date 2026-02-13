students = [
    {"name": "Ana", "grades": [8.5, 7.0, 9.0]},
    {"name": "Luis", "grades": [5.0, 4.5, 6.0]},
    {"name": "Maria", "grades": [9.5, 9.0, 10.0]},
    {"name": "Pedro", "grades": [3.0, 4.0, 2.5]},
    {"name": "Sofia", "grades": [7.0, 7.5, 8.0]},
]

def average(grades):
    total_sum = sum(grades)
    total_grades = len(grades)
    return total_sum / total_grades

all_grades = [] #the exercise didn't ask for this
for each in students:
    for c in each["grades"]:
        all_grades.append(c)

total_pass = 0
total_fail = 0
for p in students:
    grades_list = p["grades"]
    name = p["name"]
    average_mark = round(average(grades_list), 1)
    if average_mark >= 5:
        print(name, ":", round(average(grades_list), 1), "-> PASS")
        total_pass += 1
    else:
        print(name, ":", round(average(grades_list), 1), "-> FAIL")
        total_fail += 1

print("\nResults:", total_pass, "passed,", total_fail, "failed")
print("\nTotal average grade:", average(all_grades))
