def persistence(n):
    # def digital_root(n):
    # while n > 9:
    #     n = sum(map(int,str(n)))
    # return n
    # print(list(map(int,str(n))))
    # while n > 9:
    n = list(map(int,str(n)))
    print(sum(x * y for x, y in zip(n, n[1:])))







persistence(999)