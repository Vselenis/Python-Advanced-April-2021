def filter_even(iters):
    return list(filter(lambda x: x % 2 == 0, iters))


nums = [int(num) for num in input().split(' ')]
print(filter_even(nums))