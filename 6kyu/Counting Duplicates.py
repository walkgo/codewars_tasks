from collections import Counter


def duplicate_count(text):
    x = (list(text.lower()))
    counter = Counter(x)
    lst = []
    for key, val in counter.items():
        if val > 1:
            lst.append(val)
    return(len(lst))


# Best Practices
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
  