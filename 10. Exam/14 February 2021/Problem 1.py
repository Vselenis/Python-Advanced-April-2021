from collections import deque

firework_effects = deque([int(ef) for ef in input().split(", ")])
explosive_power = deque([int(ex) for ex in input().split(", ")])

palm_firework = 0
willow_firework = 0
crossette_firework = 0

counter = 0
while True:
    if firework_effects[0] <= 0:
        firework_effects.popleft()
        continue
    if explosive_power[-1] <= 0:
        explosive_power.pop()
        continue
    else:
        x = firework_effects[0]
        y = explosive_power[-1]
        mix = x + y
        if mix % 3 == 0 and mix % 5 == 0:
            firework_effects.popleft()
            explosive_power.pop()
            crossette_firework += 1
        elif mix % 3 == 0 and mix % 5 > 0:
            firework_effects.popleft()
            explosive_power.pop()
            palm_firework += 1
        elif mix % 3 > 0 and mix % 5 == 0:
            firework_effects.popleft()
            explosive_power.pop()
            willow_firework += 1
        else:
            firework_effects.append(firework_effects.popleft() - 1)

        if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
            print("Congrats! You made the perfect firework show!")
            print(f"Palm Fireworks: {palm_firework}")
            print(f"Willow Fireworks: {willow_firework}")
            print(f"Crossette Fireworks: {crossette_firework}")
            break
        if len(firework_effects) == 0 or len(explosive_power) == 0:
            print(f"Sorry. You can't make the perfect firework show.")
            if len(firework_effects) > 0:
                print(f"Firework Effects left: {', '.join([str(x) for x in firework_effects])}")
            if len(explosive_power) > 0:
                print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")
            print(f"Palm Fireworks: {palm_firework}")
            print(f"Willow Fireworks: {willow_firework}")
            print(f"Crossette Fireworks: {crossette_firework}")
            break