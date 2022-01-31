def array_diff(a, b):
    lst = []
    for i in a:
        if i not in b:
            lst.append(i)
    return(lst)


# Best Practices
def array_diff(a, b):
    return [x for x in a if x not in b]
