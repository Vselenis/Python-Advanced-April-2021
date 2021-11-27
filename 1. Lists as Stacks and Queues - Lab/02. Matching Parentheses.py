brackets = input()
matching = []

for index in range(len(brackets)):
    if brackets[index] == '(':
        matching.append(index)
    if brackets[index] == ')':
        starting_point = matching.pop()
        print(brackets[starting_point: index + 1])