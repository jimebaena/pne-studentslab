def classify_triangle(a, b, c):
    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "scalene"

print(classify_triangle(5, 5, 5))
print(classify_triangle(3, 3, 4))
print(classify_triangle(3, 4, 5))