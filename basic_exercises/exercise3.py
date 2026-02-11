temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]
maximum = 0
minimum = 100
total_temp = 0
num_temp = 0
high = 0
for c in temperatures:
    total_temp += float(c)
    num_temp += 1
    if c < minimum:
        minimum = c
    if c > maximum:
        maximum = c
    if float(c) > 17:
        high += 1
print("The temperature on Wednesday is:", temperatures[2])
print("The maximum temperature is", maximum, "and the minimum temperature is", minimum)
print("The average temperature is", round(total_temp / num_temp, 1))
print("The number of days above 17 degrees are:", high)
print("The list sorted from lowest to highest", sorted(temperatures))

