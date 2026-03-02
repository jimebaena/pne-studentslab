from Seq1 import Seq
print("-----| Practice 1, Exercise 7 |------")

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid")

sequences = [s1, s2, s3]
i = 0

for s in sequences:
    print(f"Sequence {i}: (Length: {s.len()}) {s}")
    print(f"  Bases: {s.count_base()}")
    print(f"  Rev:   {s.reverse()}")
    print(f"  Comp:   {s.complement()}")
    i += 1