def is_divisible(n,x,y):
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False


# Best Practices
def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0
