values = tuple(map(float, input().split()))
values_count = {}

for value in values:
    values_count[value] = values.count(value)

for (value, count) in values_count.items():
    print(f"{value} - {count} times")