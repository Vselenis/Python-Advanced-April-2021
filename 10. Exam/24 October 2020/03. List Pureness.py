def best_list_pureness(list_of_nums, K):
    count = 0
    dict = {}
    for num in range(K+1):

        sums = 0
        for z in range(len(list_of_nums)):
            sums += list_of_nums[z] * z

        list_of_nums.insert(0, list_of_nums.pop())
        dict[count] = sums
        sums = 0
        count += 1

    max_key = max(dict, key=dict.get)
    max_value = max(dict.values())
    return f"Best pureness {max_value} after {max_key} rotations"


# test = ([1, 2, 3, 4, 5], 10)
# result = best_list_pureness(*test)
# print(result)
#
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)
