line = [int(x) for x in input().split()]
reversed_list = []
for i in range(len(line)):
    reversed_list.append(line.pop())

print(' '.join(map(str, reversed_list)))