def read_matrix():
    rows = int(input())
    matrix = []
    for _ in range(rows):
        matrix.append([int(x) for x in input().split()])
    return matrix

matrix = read_matrix()
rows = len(matrix)

command = input()
while command != "END":
    do = command.split()[0]
    row, col, value = [int(x) for x in command.split()[1:]]
    if 0 <= col < rows and 0 <= row < rows:
        if do == "Add":
            matrix[row][col] += value
        elif do == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

    command = input()

for row in matrix:
    print(' '.join([str(num) for num in row]))
