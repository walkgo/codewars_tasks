def positive_sum(arr):
    positive_list = []
    for i in arr:
        if i > 0:
            positive_list.append(i)
    return(sum(positive_list))


# Best Practices
def positive_sum(arr):
    return sum(x for x in arr if x > 0)
