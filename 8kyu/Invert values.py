def invert(lst):
    return list(i * -1 for i in lst)


# Best Practices
def invert(lst):
    return [-x for x in lst]