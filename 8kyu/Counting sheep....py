def count_sheeps(sheep):
    return len(list(i for i in sheep if i == True))


# Best Practices
def count_sheeps(sheep):
  return sheep.count(True)
