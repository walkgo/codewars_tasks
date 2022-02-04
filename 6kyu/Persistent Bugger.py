from math import prod


def persistence(n):
    counter = 0
    while n > 9:
        counter = counter + 1
        n = list(map(int,str(n)))
        n = prod(n)
    return counter

print(persistence(4444))
# Best Practices (I doubt :/)
# import operator
# def persistence(n):
#     i = 0
#     while n>=10:
#         n=reduce(operator.mul,[int(x) for x in str(n)],1)
#         i+=1
#     return i
