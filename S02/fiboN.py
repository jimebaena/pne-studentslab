
def fibon():
    a = 0
    b = 1
    i = 2
    while i < 15:
        c = a + b
        a = b
        b = c
        i += 1
        if i == 5:
            print("The 5th element of the fibonacci series is:", c)
        elif i == 10:
            print("The 10th element of the fibonacci series is:", c)
        elif i == 15:
            print("The 15th element of the fibonacci series is:", c)
fibon()


