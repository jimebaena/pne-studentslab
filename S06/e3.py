class Seq:
    def __init__(self, bases):
        self.bases = bases
        all = ["A", "C", "G", "T"]
        total = 0
        for letter in bases:
            if letter in all:
                total += 1
        if total == len(bases):
            # Cambiado a un solo '!' para coincidir con el enunciado
            print("New sequence created!")
            self.bases = bases
        else:
            print("Error!!")
            self.bases = "ERROR!"

    def len(self):
        return len(self.bases)

    def __str__(self):
        return self.bases


def print_seqs(seq_list):
    n = 0
    for term in seq_list:
        print(f"Sequence {n}: (Length: {term.len()}) {term}")
        n += 1



def generate_seqs(pattern, number):
    seq_list = []
    for i in range(1, number + 1):
        # Al multiplicar un string (pattern) por un número (i), se repite
        new_seq = Seq(pattern * i)
        seq_list.append(new_seq)
    return seq_list


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)
print()
print("List 2:")
print_seqs(seq_list2)