def repeat_text(text, count_str):
    return text * int(count_str)


text = 'Hello'
count = 3

try:
    print(repeat_text(text, count))
except ValueError:
    print("Variable time must be an integer")