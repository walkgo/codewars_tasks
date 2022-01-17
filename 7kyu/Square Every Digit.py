def square_digits(num):
    num_list = [int(i) for i in str(num)]
    num_list2 = []
    for i in num_list:
        num_list2.append(i ** 2)
    return(int("".join(map(str, num_list2))))

        
# Best Practices
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)
    