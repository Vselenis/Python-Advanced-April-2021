def positive_nums(numbers):
    positive = []
    for number in numbers:
        if number > 0:
            positive.append(number)
    return sum(positive)


def negative_nums(numbers):
    negative = []
    for number in numbers:
        if number < 0:
            negative.append(number)
    return sum(negative)


numbers = [int(num) for num in input().split()]
print(negative_nums(numbers))
print(positive_nums(numbers))

if positive_nums(numbers) > abs(negative_nums(numbers)):
    print(f"The positives are stronger than the negatives")
elif positive_nums(numbers) < abs(negative_nums(numbers)):
    print(f"The negatives are stronger than the positives")
