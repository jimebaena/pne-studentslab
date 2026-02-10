#lines = ["AGTACACTGGT", "ACCAGTGTACT", "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"]
#print("From variable:", lines)

from dna_count import count_bases

#Option 1
f = open("dna.txt", "r") #r means we are reading
lines = f.readlines()
f.close() #don't forget to close the function

#("From file:", lines)

#Option 2
with open("dna.txt", "r") as f:
    lines = f.readlines() #automatically closed

total_number = 0

bases = {"A": 0, "C": 0, "G": 0, "T": 0}

for sequence in lines:
    sequence = sequence.strip()
    total_number += len(sequence)

    for base in sequence:
        if base in bases:
            bases[base] += 1

print("Total number of bases:", total_number)

for base, count in bases.items():
    print(f"{base}: {count}")
