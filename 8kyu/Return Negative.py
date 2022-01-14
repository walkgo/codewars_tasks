def make_negative( number ):
    if number > 0:
        return(number * -1)
    else:
        return(number)


# Best Practices
def make_negative( number ):
    return -abs(number)
