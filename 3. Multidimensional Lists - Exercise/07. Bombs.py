def read_matrix(n):
    matrix = []
    for row in range(n):
        matrix.append([int(r) for r in input().split()])
    return matrix


def read_deltas():
    deltas = [
        [0, -1],
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, 1],
        [1, 1],
        [1, 0],
        [1, -1],
    ]

    return deltas


def check_bombs():
    bombs = []
    for index in input().split():
        row = int(index[0])
        col = int(index[2])
        bombs.append([row, col])
    return bombs


def is_valid(next_row, next_col, matrix):
    if 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix):
        return True
    return False


def explode_bombs(bombs, matrix, deltas):
    for i in range(len(bombs)):
        row_index = bombs[i][0]
        col_index = bombs[i][1]
        for index in range(len(deltas)):
            next_row = row_index + deltas[index][0]
            next_col = col_index + deltas[index][1]
            if is_valid(next_row, next_col, matrix) and matrix[next_row][next_col] > 0:
                matrix[next_row][next_col] -= abs(matrix[row_index][col_index])
        matrix[row_index][col_index] = 0
    return matrix

def get_result():
    alive_cells = 0
    sum_positive = 0
    for row in matrix:
        for el in row:
            if el > 0:
                alive_cells += 1
                sum_positive += el
    print(f"Alive cells: {alive_cells}")
    print(f"Sum: {sum_positive}")
    for row in matrix:
        print(' '.join([str(el) for el in row]))



n = int(input())
matrix = read_matrix(n)
bombs = check_bombs()
deltas = read_deltas()
explode_bombs(bombs, matrix, deltas)
get_result()
