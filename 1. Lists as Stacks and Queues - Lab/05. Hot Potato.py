from collections import deque
people = input().split()
n = int(input())


people = deque(people)
index = 0
while people:
    person = people.popleft()
    index += 1
    if index == n:
        index = 0
        if people:
            print(f"Removed {person}")
            n = n % len(people)
            if n == 0:
                n = len(people)
        else:
            print(f"Last is {person}")

    else:
        people.append(person)



