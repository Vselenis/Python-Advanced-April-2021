list_of_nums = [int(x) for x in input().split(', ')]
final_index = int(input())
final_value = list_of_nums[final_index]
sum_nums = 0
for x in range(len(list_of_nums)):
    if list_of_nums[x] < final_value:
        sum_nums += list_of_nums[x]

    if x <= final_index and list_of_nums[x] == final_value:
        sum_nums += list_of_nums[x]

print(sum_nums)
