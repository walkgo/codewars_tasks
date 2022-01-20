def maskify(cc):
    return '#' * len(cc[:-4]) + cc[-4:]
        
        
# Best Practices
def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]
