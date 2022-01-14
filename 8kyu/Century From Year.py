def century(year):
    if year % 100 == 0:
        return year // 100
    else:    
        return (year // 100) + 1


# Best Practices
def century(year):
    return (year + 99) // 100
