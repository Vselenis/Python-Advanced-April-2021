def read_matrix(n):
    matr = []
    for i in range(n):
        matr.append(input().split())
    return matr


def get_commands():
    deltas = {"right": [0, 1],
              "left": [0, -1],
              "up": [-1, 0],
              "down": [1, 0]
              }
    return deltas


def search_for_player(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == "P":
                return [row, col]


def is_valid(player_row, player_col, matrix):
    if 0 <= player_row < len(matrix) and 0 <= player_col < len(matrix):
        return True
    return False


def find_coins(matrix, commands):
    player_row = search_for_player(matrix)[0]
    player_col = search_for_player(matrix)[1]
    save_path = []
    coins = 0
    while True:
        next_command = input()
        if next_command in commands:

            next_row, next_col = commands[next_command]
            player_row += next_row
            player_col += next_col
            if is_valid(player_row, player_col, matrix) and not matrix[player_row][player_col] == "X":
                save_path.append([player_row, player_col])
                coins += int(matrix[player_row][player_col])
                if coins >= 100:
                    print(f"You won! You've collected {coins} coins.")
                    break
            else:
                coins //= 2
                print(f"Game over! You've collected {coins} coins.")
                break

    print("Your path: ")
    [print(x) for x in save_path]


n = int(input())
matrix = read_matrix(n)
commands = get_commands()
find_coins(matrix, commands)
