def convert_nums(nums_list):
    result = [round(el) for el in nums_list]
    return result


nums = [float(el) for el in input().split()]
print(convert_nums(nums))
