from collections import deque


def stock_availability(*args):
    list_of_boxes = args[0]
    command = args[1]

    if command == "delivery":
        [list_of_boxes.append(el )for el in args[2:]]


    if command == "sell":
        if len(args) == 2:
           list_of_boxes.pop(0)
        elif len(args) > 2:
            if str(args[-1]).isdigit():
                for _ in range(args[-1]):
                    list_of_boxes.pop(0)
            else:
                random_list = []
                for x in list_of_boxes:
                    if x not in args[2:]:
                        random_list.append(x)
                list_of_boxes = random_list


    return list_of_boxes


print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))


