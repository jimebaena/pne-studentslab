class Seq:
    def __init__(self, bases):
        self.bases = bases
        all = ["A", "C", "G", "T"]
        total = 0
        for letter in bases:
            if letter in all:
                total += 1
        if total == len(bases):
            print("New sequence created!!")
            self.bases = bases
        else:
            print("Error!!")
            self.bases = "ERROR!"
    def __str__(self):
        return self.bases

s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
