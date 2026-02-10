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


#other form
def count_bases(sequence):
    bases = {"A": 0, "C": 0, "G": 0, "T": 0}
    for base in sequence:
        if base in bases:
            bases[base] += 1
    return bases

if __name__ == "__main__":

    sequence = input("Introduce the sequence: ")
    print("Total length:", len(sequence))

    result = count_bases(sequence)

    for base, count in result.items():
        print(f"{base}: {count}")

#to resuse any function, we can't have anything to the left