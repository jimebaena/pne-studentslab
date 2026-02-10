def count_sequence(seq):
    total_length = len(seq)
    adenine = 0
    thymine = 0
    citosine = 0
    guanine = 0
    for c in seq:
        if c == "A":
            adenine += 1
        elif c == "T":
            thymine += 1
        elif c == "C":
            citosine += 1
        elif c == "G":
            guanine += 1
    return total_length, adenine, thymine, citosine, guanine

sequence = str(input("Enter the DNA sequence:")).upper()
total, a, t, c, g = count_sequence(sequence)
print("Total length:", total)
print("A:", a)
print("T:", t)
print("C", c)
print("G", g)