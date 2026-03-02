from Seq1 import Seq

print("-----| Practice 1, Exercise 9 |------")
s = Seq()
FOLDER = "sequences/"
U5 = "U5.txt"
full_path = FOLDER + U5
s.read_fasta(full_path)

print(f"Sequence : (Length: {s.len()}) {s}")
print(f"  Bases: {s.count_base()}")
print(f"  Rev:   {s.reverse()}")
print(f"  Comp:  {s.complement()}")