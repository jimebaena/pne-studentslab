class Seq:
    def __init__(self, bases=""):
        self.bases = bases
        valid = ["A", "C", "G", "T"]
        total = 0
        for letter in bases:
            if letter in valid:
                total += 1

        if len(bases) == 0:
            print("NULL sequence created!")
            self.bases = "NULL"

        elif total == len(bases):
            print("New sequence created!")
            self.bases = bases

        else:
            print("INVALID sequence!")
            self.bases = "ERROR"

    def len(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        else:
            return len(self.bases)

    def __str__(self):
        return self.bases

    def count_base(self, bases):
        self.bases = bases
        all_bases = {"A": 0, "C": 0, "G": 0, "T": 0}
        if self.bases == "NULL" or self.bases == "ERROR":
            return all_bases
        else:
            for letter in bases:
                all_bases[letter] += 1
            return all_bases