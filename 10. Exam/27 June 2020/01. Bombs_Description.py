from collections import deque

bomb_effects = deque([int(el) for el in input().split(', ')])
bomb_casings = deque([int(num) for num in input().split(', ')])

datura_bombs = 0
cherry_bombs = 0
smoke_decoy_bombs = 0
while True:
    x = bomb_effects[0]
    y = bomb_casings[-1]
    mix = x + y


    if mix == 40:
        datura_bombs += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif mix == 60:
        cherry_bombs += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif mix == 120:
        smoke_decoy_bombs += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5

    if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_decoy_bombs >= 3:
        print("Bene! You have successfully filled the bomb pouch!")
        if len(bomb_effects) > 0:
            print(f"Bomb Effects: {', '.join([str(element) for element in bomb_effects])}")
        elif len(bomb_effects) == 0:
            print("Bomb Effects: empty")
        if len(bomb_casings) > 0:
            print(f"Bomb Casings: {', '.join([str(element) for element in bomb_casings])}")
        elif len(bomb_casings) == 0:
            print("Bomb Casings: empty")
        print(f"Cherry Bombs: {cherry_bombs}")
        print(f"Datura Bombs: {datura_bombs}")
        print(f"Smoke Decoy Bombs: {smoke_decoy_bombs}")
        break

    elif len(bomb_effects) == 0 or len(bomb_casings) == 0:
        print(f"You don't have enough materials to fill the bomb pouch.")
        if len(bomb_effects) > 0:
            print(f"Bomb Effects: {', '.join([str(element) for element in bomb_effects])}")
        elif len(bomb_effects) == 0:
            print("Bomb Effects: empty")
        if len(bomb_casings) > 0:
            print(f"Bomb Casings: {', '.join([str(element) for element in bomb_casings])}")
        elif len(bomb_casings) == 0:
            print("Bomb Casings: empty")
        print(f"Cherry Bombs: {cherry_bombs}")
        print(f"Datura Bombs: {datura_bombs}")
        print(f"Smoke Decoy Bombs: {smoke_decoy_bombs}")
        break
