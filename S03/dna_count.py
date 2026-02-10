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
seq = input("Introduce the sequence: ").upper()
print(f"Total length: {len(seq)}")
bases = {"A": 0, "C": 0, "G": 0, "T": 0}
for base in seq:
    if base in bases:
        bases[base] += 1
for base, count in bases.items():
    print(f"{base}: {count}")