def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:1] + sorted(numbers)[1:2])


# Best Practices
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])