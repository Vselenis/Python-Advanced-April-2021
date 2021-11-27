from collections import deque
already_paid = deque()
while True:
    name = input()
    if name == "End":
        print(f"{len(already_paid)} people remaining.")
        break
    if name == "Paid":
        while already_paid:
            print(already_paid.popleft())
    else:
        already_paid.append(name)
