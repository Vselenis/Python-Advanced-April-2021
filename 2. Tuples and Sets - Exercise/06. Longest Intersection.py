n = int(input())
intersections = []
for _ in range(n):
    data = input()
    first_data, second_data = data.split('-')
    start, stop = [int(el) for el in first_data.split(",")]
    first_sequence = range(start, stop + 1)
    start, stop = [int(el) for el in second_data.split(",")]
    second_sequence = range(start, stop + 1)
    intersection = set(first_sequence).intersection(second_sequence)
    intersections.append(intersection)

longest = sorted(intersections, key=lambda x: -len(x))
print(f"Longest intersection is {list(longest[0])} with length {len(longest[0])}")