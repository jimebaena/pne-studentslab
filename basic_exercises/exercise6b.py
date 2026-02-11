def classify_triangle(a, b, c):
    if a == b:
        if a == c:
            result = "equilateral"
        elif a != c:
            result = "isosceles"
    elif a != b:
        if a == c:
            result = "isosceles"
        elif a != c:
            if b == c:
                result = "isosceles"
            elif b != c:
                result = "scalene"
    return result

print("The triangle is:", classify_triangle(3,3,3))