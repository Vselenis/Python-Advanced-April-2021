def read_matrix(is_test=False):
    if is_test:
        return [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12],
        ]
    else:
        size = int(input())
        matrix = []
        for row_index in range(size):
            row = [int(x) for x in input().split()]
            matrix.append(row)

        return matrix


def get_primary_diagonal_sum(matrix):
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]
    return diagonal_sum


# def get_sum_below_primary_diagonal(matrix):
#     the_sum = 0
#     size = len(matrix)
#     for r in range(size):
#         for c in range(size):
#             if c <= r:
#                 the_sum += matrix[r][c]
#     return matrix


print(get_primary_diagonal_sum(read_matrix()))
# print(get_sum_below_primary_diagonal(read_matrix()))
