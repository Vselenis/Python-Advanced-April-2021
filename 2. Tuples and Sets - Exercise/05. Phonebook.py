personal_info = input()
phonebook = {}
while not personal_info.isdigit():
    person, number = personal_info.split("-")
    phonebook[person] = number
    personal_info = input()

n = int(personal_info)
for _ in range(n):
    check = input()
    if phonebook.get(check):
        print(f"{check} -> {phonebook[check]}")
    else:
        print(f"Contact {check} does not exist.")
