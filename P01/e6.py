from Seq1 import Seq
print("-----| Practice 1, Exercise 6 |------")

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid")

sequences = [s1, s2, s3]

i = 0
for s in sequences:
    print(f"Sequence {i}: (Length: {s.len()}) {s}")
    dict_bases = s.count_base()
    print(f"  Bases: {dict_bases}")
    i += 1