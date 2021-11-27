def min_number(x):
    min_n = min(x)
    return f'The minimum number is {min_n}'


def max_number(x):
    max_n = max(x)
    return f'The maximum number is {max_n}'


def sum_numbers(x):
    sum_n = sum(x)
    return f'The sum number is: {sum_n}'


numbers = [int(num) for num in input().split()]
print(min_number(numbers))
print(max_number(numbers))
print(sum_numbers(numbers))
