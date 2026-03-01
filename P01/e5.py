from Seq1 import Seq

print("-----| Practice 1, Exercise 5 |------")

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid")


print(f"Sequence 1: (Length: {s1.len()}) {s1}")
type_bases = s1.count_base()
for key, value in type_bases.items():
    print(f"{key}: {value}")
print(f"Sequence 2: (Length: {s2.len()}) {s2}")
type_bases = s2.count_base()
for key, value in type_bases.items():
    print(f"{key}: {value}")
print(f"Sequence 3: (Length: {s3.len()}) {s3}")
type_bases = s3.count_base()
for key, value in type_bases.items():
    print(f"{key}: {value}")