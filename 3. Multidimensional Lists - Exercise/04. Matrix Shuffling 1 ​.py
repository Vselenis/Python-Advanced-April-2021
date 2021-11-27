def create_matrix(r):
    m = []
    for _ in range(r):
        m.append([x for x in input().split()])
    return m


def printing(mat):
    for r in range(rows):
        for c in range(columns):
            print(mat[r][c], end=' ')
        print()


rows, columns = map(int, input().split())
matrix = create_matrix(rows)
line = input()

while line != 'END':
    todo = line.split()
    if len(todo) == 5 and todo[0] == 'swap':
        row_1 = int(todo[1])
        col_1 = int(todo[2])
        new_row_1 = int(todo[3])
        new_col_1 = int(todo[4])
        try:
            matrix[row_1][col_1], matrix[new_row_1][new_col_1] = matrix[new_row_1][new_col_1], matrix[row_1][col_1]
            printing(matrix)
        except IndexError:
            print('Invalid input!')
    else:
        print('Invalid input!')
    line = input()