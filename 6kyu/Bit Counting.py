def count_bits(n):
    return len([i for i in list(bin(n)) if i == '1'])


# Best Practices
def countBits(n):
    return bin(n).count("1")
