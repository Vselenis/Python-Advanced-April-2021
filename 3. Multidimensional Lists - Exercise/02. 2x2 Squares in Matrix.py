rows, columns = map(int, input().split())


def read_matrix():
    matrix = []
    for _ in range(rows):
        row = [x for x in input().split()]
        matrix.append(row)

    return matrix


def check_elements_are_equal(row, col, matr):
    current_element = matr[row][col]
    element_right = matr[row][col + 1]
    element_bottom = matr[row + 1][col]
    element_bottom_right = matr[row + 1][col + 1]
    if current_element == element_right and element_right == element_bottom and element_bottom_right == element_bottom:
        return True
    return False


matrix = read_matrix()

counter = 0
for row_index in range(rows - 1):
    for col_index in range(columns - 1):
        if check_elements_are_equal(row_index, col_index, matrix):
            counter += 1

print(counter)