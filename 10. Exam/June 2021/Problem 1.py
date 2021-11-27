chocolates = [int(el) for el in input().split(", ")]
cups_of_milk = [int(element) for element in input().split(", ")]




counter = 0

while True:
    if counter == 5:
        print("Great! You made all the chocolate milkshakes needed!")
        if len(chocolates) > 0:
            print(f"Chocolate: {', '.join([str(choco) for choco in chocolates])}")
        else:
            print("Chocolate: empty")
        if len(cups_of_milk) > 0:
            print(f"Milk: {', '.join([str(milk) for milk in cups_of_milk])}")
        else:
            print("Milk: empty")
        break

    if len(chocolates) == 0:
        print("Not enough milkshakes.")
        print("Chocolate: empty")
        if len(cups_of_milk) > 0:
            print(f"Milk: {', '.join([str(milk) for milk in cups_of_milk])}")
        else:
            print("Milk: empty")
        break

    if len(cups_of_milk) == 0:
        print("Not enough milkshakes.")
        if len(chocolates) > 0:
            print(f"Chocolate: {', '.join([str(choco) for choco in chocolates])}")
        else:
            print("Chocolate: empty")
        print("Milk: empty")
        break

    chocolate = chocolates[-1]
    cup_of_milk = cups_of_milk[0]

    if chocolate <= 0:
        chocolates.pop()
        continue
    if cup_of_milk <= 0:
        cups_of_milk.pop(0)
        continue

    elif chocolate == cup_of_milk:
        counter += 1
        chocolates.pop()
        cups_of_milk.pop(0)
    else:
        cup = cups_of_milk.pop(0)
        cups_of_milk.append(cup)
        chocolates[-1] -= 5
