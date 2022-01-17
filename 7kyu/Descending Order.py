def descending_order(num):
    num_list = [i for i in str(num)]
    num_list.sort(reverse=True)
    return(int(''.join((num_list))))


# Best Practices
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
