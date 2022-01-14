def digitize(n):
    return list(int(i) for i in str(n))[::-1]


# Best Practices
def digitize(n):
    return map(int, str(n)[::-1])