def fibosum(n):
    a = 0
    b = 1
    i = 2
    sum = 1
    while i < n:
        c = a + b
        a = b
        b = c
        i += 1
        sum += c
    return sum

print("The sum of the first 5 elements of fibonacci series is:", fibosum(5))
print("The sum of the first 10 elements of fibonacci series is:", fibosum(10))
