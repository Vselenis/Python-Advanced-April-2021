def input_to_list(count):
    lines = set()
    for _ in range(count):
        lines.add(input())
    return lines

n = int(input())
reservations = input_to_list(n)

guests = input()
while guests != "END":
    if guests in reservations:
        reservations.remove(guests)
    guests = input()

print(len(reservations))
reservations = sorted(reservations)
[print(x) for x in reservations]
