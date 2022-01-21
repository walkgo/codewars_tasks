def get_sum(a,b):
    x = []
    if b < 0 and a > 0 or a > b:
        for i in range(b, a + 1):
            x.append(i)
        return sum(x)
    else:
        for i in range(a, b + 1):
            x.append(i)
        return sum(x)


# Best Practices
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))
