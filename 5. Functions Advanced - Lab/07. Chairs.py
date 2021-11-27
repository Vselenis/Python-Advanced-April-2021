def calc_combinations(names, n, combos=[]):
    if len(combos) == n:
        print(", ".join(combos))
        return

    for i in range(len(names)):
        name = names[i]
        combos.append(name)
        calc_combinations(names[i + 1:], n, combos)
        combos.pop()


names = input().split(", ")
n = int(input())
calc_combinations(names, n)
