dna = "ATGCGATCGATCGATCGATCGA"
print("The total length of the string is:", len(dna))
print("The first five characters are: ", dna[:5])
print("The last three characters are: ", dna[-3:])
print("The string convert to lowercase: ", dna.lower())
print("The number of times that the string 'ATC' appears is: ", dna.count("ATC"))
print("The dna sequence convert into a rna sequence: ", dna.replace("T", "U"))
