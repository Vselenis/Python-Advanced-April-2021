DEFAULT_ROWS_COUNT = 6
DEFAULT_COLUMNS_COUNT = 7

def get_player_choice_func(is_test=False):
    def get_player_choice(player):
        print(f"Player {player},please choose a column")
        return int(input()) - 1

    choices_for_test= [1,2,2,3,3,4,1,5]
    choices_for_test_index = 0

    def get_player_choice_for_test(player):
        nonlocal choices_for_test_index
        print(f"Player {player},please choose a column")
        choice = choices_for_test[choices_for_test_index]
        choices_for_test_index += 1
        return choice -1

    if is_test:
        return get_player_choice_for_test
    else:
        return get_player_choice



def check_win_condition():
    pass

def get_lowest_free_row_index(board, column_index):
    rows_count = len(board)
    for rows_index in range(rows_count - 1, - 1, -1):
        if board[rows_index][column_index] == 0:
            return rows_index
    return None


def apply_player_choice(board, column_index , player):
    row_index = get_lowest_free_row_index(board,column_index)
    board[row_index][column_index] = player


def play(board, player=1):
    while True:
        player_choice = get_player_choice(player)
        apply_player_choice(board, player_choice, player)
        print_board(board)
        if check_win_condition():
            break
        player = 2 if player == 1 else 1
    # else:
    #     play(board, player=2)



def create_board(rows_count=DEFAULT_ROWS_COUNT, columns_count=DEFAULT_COLUMNS_COUNT):
    return [[0] * columns_count for _ in range(rows_count)]


get_player_choice = get_player_choice_func(is_test=True)
board = create_board()
play(board)