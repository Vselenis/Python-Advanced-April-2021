def nums(numbers, command):
    odd = []
    even = []
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    if command == 'Odd':
        return sum(odd) * len(numbers)
    if command == 'Even':
        return sum(even) * len(numbers)


command = input()
numbers = [int(num) for num in input().split()]
print(nums(numbers, command))
