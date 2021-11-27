def read_matrix(n):
    matr = []
    for row in range(n):
        rows = []
        for x in input().split():
            rows += x
        matr.append(rows)
    return matr


def get_direction():
    deltas = {"right": [0, 1],
              "left": [0, -1],
              "up": [-1, 0],
              "down": [1, 0]
              }
    return deltas

def search_for_position(matrix):
    snake = []
    burrow = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == "S":
                snake.append(row)
                snake.append(col)
            elif matrix[row][col] == "B":
                burrow.append([row, col])
    return snake, burrow

def is_valid(snake_row, snkae_col, matrix):
    if 0 <= snake_row < len(matrix) and 0 <= snkae_col < len(matrix):
        return True
    return False

def play_game():
    food = 0

    command = input()
    snake_row = snake_position[0]
    snake_col = snake_position[1]
    while True:
        command_row, command_column = get_direction()[command]
        matrix[snake_row][snake_col] = '.'
        snake_row += command_row
        snake_col += command_column

        if not is_valid(snake_row, snake_col, matrix):
            print(f"Game over!")
            print(f"Food eaten: {food}")
            for row in matrix:
                print(''.join([x for x in row]))
            break

        if matrix[snake_row][snake_col] == '*':
            food += 1
        elif matrix[snake_row][snake_col] == 'B':
            matrix[snake_row][snake_col] = '.'
            burrow_position.remove([snake_row, snake_col])
            snake_row, snake_col = burrow_position.pop()

        if food == 10:
            print(f"You won! You fed the snake.")
            print(f"Food eaten: {food}")
            matrix[snake_row][snake_col] = 'S'
            for row in matrix:
                print(''.join([x for x in row]))
            break
        command = input()

n = int(input())
matrix = read_matrix(n)
snake_position, burrow_position = search_for_position(matrix)
play_game()
