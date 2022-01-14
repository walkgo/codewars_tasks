def find_outlier(integers):
    even = filter(lambda n: n % 2 == 0, integers)
    odd = filter(lambda n: n % 2 == 1, integers)
    even_list = list(even)
    odd_list = list(odd)
    if len(odd_list) == 1:
        return(odd_list[0])
    else:
        return(even_list[0])


#Best Practices
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]
