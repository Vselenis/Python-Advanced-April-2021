
class ValueCannotBeNegativeError(Exception):
    def __init__(self,value):
        super().__init__(f"{value} is negative")

def validate_positive_nums(numbers):
    for number in numbers:
        if number < 0:
            raise ValueCannotBeNegativeError(number)

numbers = [1, 4, -5, 3, 10]

validate_positive_nums(numbers)
print('Numbers are positive')