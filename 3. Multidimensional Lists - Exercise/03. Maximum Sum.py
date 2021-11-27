import sys

rows, columns = map(int, input().split())


def read_matrix():
    matrix = []
    for _ in range(rows):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix

matrix = read_matrix()

biggest_sum = - sys.maxsize
best_matrix = []

for row in range(rows - 2):
    for col in range(columns - 2):
        sub_matrix = []
        current_sum = 0
        row_counter = 0
        for r in range(row, row + 3):
            sub_matrix.append([])
            for c in range(col, col + 3):
                sub_matrix[row_counter].append(matrix[r][c])
                current_sum += matrix[r][c]
            row_counter += 1
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            best_matrix = sub_matrix

print(f'Sum = {biggest_sum}')
for row in best_matrix:
    print(" ".join([str(x) for x in row]))

