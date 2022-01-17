def is_square(n):
    square_root = n ** 0.5
    return n > -1 and square_root % 1 == 0;


# Best Practices
import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;
