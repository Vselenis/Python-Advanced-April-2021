from collections import deque


def list_manipulator(*args):
    list_of_numbers = deque(args[0])
    command = args[1]
    order = args[2]
    if command == 'add':
        elements = list(args[3:])
        for num in range(len(elements)):
            if order == 'beginning':
                list_of_numbers.appendleft(elements.pop())
            elif order == 'end':
                list_of_numbers.append(elements[num])

    elif command == 'remove':
        if order == 'beginning':
            if len(args) == 3:
                list_of_numbers.popleft()
            elif len(args) == 4:
                for _ in range(args[-1]):
                    list_of_numbers.popleft()
        if order == 'end':
            if len(args) == 3:
                list_of_numbers.pop()
            elif len(args) == 4:
                for _ in range(args[-1]):
                    list_of_numbers.pop()
    return list(list_of_numbers)

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

