def sum_mul(n, m):
    if n <= 0 or m <= 0:
            return("INVALID")
    else:
        sum = 0
        for i in range(n, m):
            if i % n == 0:
                sum += i
        return(sum)


# Best Practices
def sum_mul(n, m):
    if m>0 and n>0:
        return sum(range(n, m, n))
    else:
        return 'INVALID'
