import sys

def read_matrix():
    (rows_count, columns_count) = map(int, input().split(', '))
    matrix = []
    for row_index in range(rows_count):
        row = list(map(int, input().split(', ')))
        matrix.append(row)
    return matrix


def submatrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    first_row = []
    second_row = []
    max_sum = - sys.maxsize
    for column in range(columns - 1, 0, -1):
        for row in range(rows - 1, 0, -1):
            sum_values = matrix[row][column] + matrix[row][column-1] + matrix[row - 1][column] + matrix[row-1][column - 1]
            if sum_values >= max_sum:
                max_sum = sum_values
                second_row = matrix[row][column-1], matrix[row][column]
                first_row = matrix[row-1][column - 1], matrix[row - 1][column]

    return f'{" ".join(map(str, first_row)) }\n{" ".join(map(str, second_row))}\n{max_sum}'

print(submatrix(read_matrix()))
