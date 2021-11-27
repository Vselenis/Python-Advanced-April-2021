strings = input().split()

main_colors = ["red", "yellow", "blue"]
secondary_colors = {"orange": ("red", "yellow"), "purple": ("blue", "red"), "green": ("blue", "yellow")}


made_colors = []

while strings:
    first_element = strings.pop(0)
    second_element = ''

    if strings:
        second_element = strings.pop()

    first_combination = first_element + second_element
    second_combination = second_element + first_combination

    if first_combination in main_colors or first_combination in secondary_colors:
        made_colors.append(first_combination)
    elif second_combination in made_colors or second_combination in secondary_colors:
        made_colors.append(second_combination)
    else:
        if len(first_combination) > 0:
            strings.insert(len(strings) // 2, first_combination[:-1])
        if len(first_combination) > 0:
            strings.insert(len(strings) // 2, secondary_colors[:-1])

for i in range(len(made_colors) -1,-1,-1):
    current = made_colors[i]
    if current in secondary_colors and any(x not in made_colors for x in secondary_colors[current]):
        del made_colors[i]
print(made_colors)