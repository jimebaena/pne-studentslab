from pathlib import Path
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

    def count_base(self):
        all_bases = {"A": 0, "C": 0, "G": 0, "T": 0}
        if self.bases == "NULL" or self.bases == "ERROR":
            return all_bases
        else:
            for letter in self.bases:
                all_bases[letter] += 1
            return all_bases

    def reverse(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases
        else:
            return self.bases[::-1]

    def complement(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases
        new = ""
        for letter in self.bases:
            if letter == "A":
                new += "T"
            elif letter == "T":
                new += "A"
            elif letter == "C":
                new += "G"
            elif letter == "G":
                new += "C"
        return new

    def read_fasta(self, filename):
        try:
            file_contents = Path(filename).read_text()
            t = file_contents.find("\n")
            sequence = file_contents[t:].replace("\n", "").strip()
            self.__init__(sequence) #volvemos a llamar al iniciador

        except FileNotFoundError:
            print(f"Error: file not found {filename}")
            self.bases = "ERROR"

    def get_most_frequent(self):
        counts = self.count_base()
        max_base = ""
        max_value = -1
        for base in counts:
            if counts[base] > max_value:
                max_value = counts[base]
                max_base = base
        return max_base