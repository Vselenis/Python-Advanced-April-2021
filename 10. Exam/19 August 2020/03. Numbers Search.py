def numbers_searching(*args):
    args = sorted(args)
    size = len(args)
    repeated = []
    for i in range(size):
        k = i + 1
        for j in range(k, size):
            if args[i] == args[j] and args[i] not in repeated:
                repeated.append(args[i])

    missing_num = [x for x in range(args[0], args[-1] + 1) if x not in args]
    return [missing_num[0], repeated]



print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))