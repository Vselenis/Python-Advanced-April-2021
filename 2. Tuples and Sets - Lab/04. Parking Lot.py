def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())
    return lines

def print_result(parking):
    if parking:
        for car in parking:
            print(car)
    else:
        print("Parking Lot is Empty")

n = int(input())
parking_info = input_to_list(n)
parking = set()

for line in parking_info:
    command, car_num = line.split(', ')
    if command == "IN":
        parking.add(car_num)
    else:
        parking.remove(car_num)

print_result(parking)
