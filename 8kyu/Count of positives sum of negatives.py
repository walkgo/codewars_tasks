def count_positives_sum_negatives(arr):
    positive = []
    negative = []
    if bool(arr) == False:
            return([])
    else:
        for i in arr:
            if i > 0:
                positive.append(i)
            if i < 0:
                negative.append(i)
        result = [len(positive), sum(negative)]
        return(result)


# Best Practices
def count_positives_sum_negatives(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
      if x > 0:
          pos += 1
      if x < 0:
          neg += x
    return [pos, neg]