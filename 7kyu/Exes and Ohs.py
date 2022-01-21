def xo(s):
    x = []
    o = []
    for i in list(s.lower()):
        if i in 'x':
            x.append(i)
        elif i in 'o':
            o.append(i)
    if len(x) == len(o):
        return True
    else:
        return False


# Best Practices
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
