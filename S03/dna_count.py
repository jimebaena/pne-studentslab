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

#to re-use any function, we can't have anything to the left