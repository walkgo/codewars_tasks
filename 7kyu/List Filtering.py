def filter_list(l):
    x = []
    for i in l:
        if type(i) == int:
            x.append(i)
    return(x)


# Best Practices
def filter_list(l):
    return [i for i in l if not isinstance(i, str)]