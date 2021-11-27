def read_matrix():
    (rows_count, columns_count) = map(int, input().split(', '))
    matrix = []
    sum_elements = 0
    for row_index in range(rows_count):
        row = list(map(int, input().split(', ')))
        sum_elements += sum(row)
        matrix.append(row)
    return matrix, sum_elements



matrix, sums = read_matrix()



print(sums)
print(matrix)