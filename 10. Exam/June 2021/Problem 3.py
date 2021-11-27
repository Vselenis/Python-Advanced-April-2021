def math_operations(*args, **kwargs):
    list_of_numbers = [num for num in args]
    while list_of_numbers:
        for i in range(1, 5):
            if len(list_of_numbers) == 0:
                break
            if i == 1:
                kwargs["a"] += list_of_numbers[0]
                list_of_numbers.pop(0)
            elif i == 2:
                kwargs["s"] -= list_of_numbers[0]
                list_of_numbers.pop(0)
            elif i == 3:
                if list_of_numbers[0] != 0:
                    kwargs["d"] /= list_of_numbers[0]
                list_of_numbers.pop(0)
            else:
                kwargs["m"] *= list_of_numbers[0]
                list_of_numbers.pop(0)

    return kwargs





print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))