n = int(input())
sequence = []

for _ in range(n):
    command = [int(x) for x in input().split()]
    if command[0] == 1:
        add_me = command[1]
        sequence.append(command[1])
    if sequence:
        if command[0] == 2:
            sequence.pop()
        elif command[0] == 3:
            print(max(sequence))
        elif command[0] == 4:
            print(min(sequence))

print(', '.join(map(str, reversed(sequence))))
