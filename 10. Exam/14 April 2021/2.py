def read_matrix():
    m = []
    n = int(input())
    for _ in range(n):
        m.append([x for x in input()])
    return m

def find_player(matr):
    for row in range(len(matr)):
        for column in range(len(matr)):
            if matr[row][column] == "P":
                return row, column

def directions():
    side = {"up": [-1, 0],
            "down": [1, 0],
            "right": [0, 1],
            "left": [0, -1]}

    return side

def is_valid(row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False

def play_game(special_word):
    side = directions()
    total_moves = int(input())
    player_row, player_col = find_player(matrix)
    for _ in range(total_moves):
        move = input()
        matrix[player_row][player_col] = "-"
        player_row += side[move][0]
        player_col += side[move][1]
        if is_valid(player_row, player_col):
            if matrix[player_row][player_col] == "-":
                matrix[player_row][player_col] = 'P'
            else:
                special_word += matrix[player_row][player_col]
                matrix[player_row][player_col] = 'P'
        else:
            special_word = special_word[:-1]
            player_row -= side[move][0]
            player_col -= side[move][1]
            matrix[player_row][player_col] = 'P'

    print(special_word)
    for r in range(len(matrix)):
        print("".join([x for x in matrix[r]]))








special_word = input()
matrix = read_matrix()
play_game(special_word)