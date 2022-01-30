from collections import Counter


def find_it(seq):
    counter = Counter(seq)
    for key, val in counter.items():
        if val % 2 != 0:
            return(key)


# Best Practices
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
