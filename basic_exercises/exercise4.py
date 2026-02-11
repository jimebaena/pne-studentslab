def letter_grades(grade):
    if grade >= 9 and grade <= 10:
        result = "A"
    elif grade >= 7 and grade <= 8.9:
        result = "B"
    elif grade >= 5 and grade <= 6.9:
        result = "C"
    elif grade >= 3 and grade <= 4.9:
        result = "D"
    elif grade >= 0 and grade <= 2.9:
        result = "F"
    else:
        result = "Not valid grade"
    return result

numeric_grade = float(input("Enter the numeric grade:"))
print("The final mark is:", letter_grades(numeric_grade))