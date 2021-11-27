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


def get_primary_diagonals_sum(matrix):
    size = len(matrix)
    main_diagonal = 0
    opposite_diagonal = 0
    for i in range(len(matrix)):
        main_diagonal += matrix[i][i]
        opposite_diagonal += matrix[i][size - i - 1]
    return abs(main_diagonal - opposite_diagonal)


print(get_primary_diagonals_sum(read_matrix()))
