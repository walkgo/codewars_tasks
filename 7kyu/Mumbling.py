def accum(s):
    x = list(s.lower())
    y = []
    for i, v in enumerate(x):
        y.append(v * (i+1))
    return("-".join(y).title())


# Best Practices
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
