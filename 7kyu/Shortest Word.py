def find_short(s):
    x = [len(i) for i in s.split(' ')]
    return min(x)


# Best Practices
def find_short(s):
    return min(len(x) for x in s.split())
