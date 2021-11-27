random_string = input()
count_symbols = {}

for string in random_string:
    if string not in count_symbols:
        count_symbols[string] = 1
    else:
        count_symbols[string] += 1
count_symbols = dict(sorted(count_symbols.items(), key=lambda x: x[0]))
[print(f"{key}: {value} time/s") for (key, value) in count_symbols.items()]
