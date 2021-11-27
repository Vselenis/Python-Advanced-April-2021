from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectars = deque([int(x) for x in input().split()])
symbols = deque([x for x in input().split()])
counter = 0


while True:
    bee = working_bees.popleft()
    nectar = nectars.pop()

    if bee <= nectar:
        symbol = symbols[0]
        if symbol == "+":
            counter += abs(bee + nectar)
        elif symbol == "-":
            counter += abs(bee - nectar)
        elif symbol == "/":
            if bee != 0:
                x = bee / nectar
                counter += abs(x)
        elif symbol == "*":
            x = bee * nectar
            counter += abs(x)

        symbols.popleft()

    elif bee > nectar:
        working_bees.appendleft(bee)

    if len(working_bees) == 0 and len(nectars) == 0:
        print(f"Total honey made: {counter}")
        break

    if len(working_bees) == 0:
        print(f"Total honey made: {counter}")
        print(f"Nectar left: {', '.join([str(n) for n in nectars])}")
        break
    if len(nectars) == 0:
        print(f"Total honey made: {counter}")
        print(f"Bees left: {', '.join([str(b) for b in working_bees])}")
        break