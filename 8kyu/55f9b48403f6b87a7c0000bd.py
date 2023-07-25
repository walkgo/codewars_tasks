def paperwork(n, m):
    if n <= 0 or m <= 0:
        return 0
    else:
        return n * m


# Best Practices
def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0
