def read_matrix():
    matr = []
    for i in range(5):
        matr.append(input().split())
    return matr

def make_moves():
    moves = {"left": (0, -1),
             "up": (-1, 0),
             "right": (0, 1),
             "down": (1, 0)
             }
    return moves

def find_player():
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "A":
                return [row, col]

def is_valid(player_row, player_col):
    if 0 <= player_row < len(matrix) and 0 <= player_col < len(matrix):
        return True
    return False

def find_targets():
    targets = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "x":
                targets.append([row, col])
    return targets


def play_game():
    player_row = find_player()[0]
    player_col = find_player()[1]
    n = int(input())
    count_targets = 0
    targ = []
    for _ in range(n):
        command = [pos for pos in input().split()]
        direction = command[1]

        if command[0] == "move":
            steps = int(command[2])
            for step in range(steps):
                row = player_row + make_moves()[direction][0]
                col = player_col + make_moves()[direction][1]
                if is_valid(row, col):
                    player_row = row
                    player_col = col

                if matrix[row][col] == "x":
                    break

                elif not is_valid(player_row, player_col):
                    break




        elif command[0] == "shoot":
            shot_row = player_row
            shot_col = player_col
            while is_valid(shot_row, shot_col):
                shot_row += moves[direction][0]
                shot_col += moves[direction][0]
                if not is_valid(shot_row, shot_col):
                    break
                if matrix[shot_row][shot_col] == "x":
                    count_targets += 1
                    targ.append([shot_row, shot_col])
                    targets.remove([shot_row, shot_col])

                    if len(targets) == 0:
                        print(f"Training completed! All {count_targets} targets hit.")

                        for x in targ:
                            print(x)
                        break
                    else:
                        break
    if len(targets) > 0:
        print(f"Training not completed! {len(targets)} targets left.")
        for t in targ:
            print(t)



matrix = read_matrix()
moves = make_moves()
targets = find_targets()
play_game()