myStr = input()

open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            position = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[position] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


print(check(myStr))
