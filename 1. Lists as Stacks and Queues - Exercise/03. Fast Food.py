from collections import deque
food = int(input())
queue = deque([int(x) for x in input().split()])
print(max(queue))


while queue:
    current_order = queue.popleft()
    if food >= current_order:
        food -= current_order
    else:
        queue.appendleft(current_order)
        print(f"Orders left: {' '.join(map(str, list(queue)))}")
        break

if not queue:
    print("Orders complete")

