def seq_ping():
    print("OK")


from pathlib import Path

def seq_read_fasta(filename):
    try:
        file_contents = Path(filename).read_text()
        t = file_contents.find("\n")
        sequence = file_contents[t:].replace("\n", "")
        return sequence
    except FileNotFoundError:
        print(f"Error: file not found {filename}")
        return ""

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    counts = {
        'A': seq.count('A'),
        'T': seq.count('T'),
        'C': seq.count('C'),
        'G': seq.count('G')
    }
    return counts


def seq_reverse(seq, n):
    fragment = seq[:n]
    reverse_fragment = fragment[::-1]
    return reverse_fragment


def seq_complement(seq):
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    complement_seq = ""
    for base in seq:
        complement_seq += complement_map.get(base, base)

    return complement_seq
