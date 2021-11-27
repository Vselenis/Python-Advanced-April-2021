def read_matrix(n):
    matr = []
    for _ in range(n):
        matr.append([0 for x in range(n)])
    for i in range(len(bombs)):
        matr[bombs[i][0]][bombs[i][1]] = "*"
    return matr


def search_bombs():
    num_of_bombs = int(input())
    bombs = []
    for _ in range(num_of_bombs):
        b = input().split(', ')
        row_bomb = int(b[0][1:])
        col_bomb = int(b[1][:-1])
        bombs.append((row_bomb, col_bomb))
    return bombs


def is_valid(row_index, column_index):
    if 0 <= row_index < len(matrix) and 0 <= column_index < len(matrix) and matrix[row_index][column_index] != "*":
        return True
    return False


def make_moves():
    positions = [
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1)
    ]
    return positions


def play_game():
    for i in range(len(bombs)):
        row_of_bomb = bombs[i][0]
        column_of_bomb = bombs[i][1]
        for index in range(len(make_moves())):
            row_index = row_of_bomb + make_moves()[index][0]
            column_index = column_of_bomb + make_moves()[index][1]
            if is_valid(row_index, column_index):
                matrix[row_index][column_index] += 1

    return print_result()

def print_result():
    for row in matrix:
        print(" ".join([str(x) for x in row]))


n = int(input())
bombs = search_bombs()
matrix = read_matrix(n)
# print(matrix)
play_game()
