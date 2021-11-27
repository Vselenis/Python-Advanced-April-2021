PLAYER = 'P'
BUNNY = 'B'
EMPTY = '.'


def read_input():
    lair = [['.', '.', '.', '.', '.', '.', '.', 'B'],
            ['.', '.', '.', 'B', '.', '.', '.', '.'],
            ['.', '.', '.', '.', 'B', '.', '.', 'B'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', 'P', '.', '.', '.', '.', '.']
            ]

    direction = "ULLL"
    return (lair, direction)


def get_bunnies(lair):
    bunnies = []
    for row_index in range(len(lair)):
        for column_index in range(len(lair[0])):
            if lair[row_index][column_index] == BUNNY:
                bunnies.append((row_index, column_index))
    return bunnies


def get_player(lair):
    for row_index in range(len(lair)):
        if PLAYER in lair[row_index]:
            column_index = lair[row_index].index(PLAYER)
            return (row_index, column_index)


def get_next_move(player, dir):
    dir_deltas = []
    (row_index, column_index) = player
    pass


def spread_bunnies(lair, bunnies):
    pass


def is_loss():


def is_win():


def play_game(lair, bunnies, player, directions):
    row_index, column_index = player
    for dir in directions:
        spread_bunnies(lair, bunnies)
        next_row_index, next_column_index = get_next_move((row_index, column_index), dir)
        if is_win(lair, (next_row_index, next_column_index)):
            print_result(lair, row_index, column_index, is_win=True)
            break
        elif is_loss(lair, (next_row_index, next_column_index)):
            print_result(lair, row_index, column_index, is_win=False)
            break
        lair[next_row_index, next_column_index] = PLAYER
        lair[row_index][column_index] = EMPTY
        row_index, column_index = next_row_index, next_column_index


lair, directions = read_input()
bunnies = get_bunnies(lair)
player = get_player(lair)
