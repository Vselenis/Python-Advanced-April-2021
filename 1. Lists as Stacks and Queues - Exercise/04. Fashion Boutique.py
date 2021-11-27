box = list(map(int, input().split()))
capacity = int(input())

counter_racks = 1
current_capacity = capacity

while len(box) > 0:
    currrent_clothes = box.pop()

    if currrent_clothes <= current_capacity:
        current_capacity -= currrent_clothes
    else:
        counter_racks += 1
        current_capacity = capacity
        current_capacity -= currrent_clothes

print(counter_racks)