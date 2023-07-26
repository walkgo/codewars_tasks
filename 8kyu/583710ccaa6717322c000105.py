def simple_multiplication(number) :
    if number % 2 == 0:
        print(number * 8)
    else:
        print(number * 9)


#Best
def simple_multiplication(number) :
    return number * 9 if number % 2 else number * 8
