def distinct(seq):
    temp = []
    for i in seq:
        if i not in temp:
            temp.append(i)
    return temp


# Best Practices
def distinct(seq):
    return sorted(set(seq), key = seq.index)
