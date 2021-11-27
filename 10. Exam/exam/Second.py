ALICE = "A"
RABBIT_HOLE = 'R'

def read_matrix():
  m = []
  n = int(input())
  for row in range(n):
    new_line = []
    for x in input().split():
      if x.isnumeric():
        x = int(x)
      new_line.append(x)
    m.append(new_line)
  return m


def find_alice_position(territory):
    for row_index in range(len(territory)):
        for column_index in range(len(territory[0])):
            if territory[row_index][column_index] == ALICE:
                return (row_index, column_index)

def find_rabbit_hole_position(territory):
    for row_index in range(len(territory)):
        for column_index in range(len(territory[0])):
            if territory[row_index][column_index] == RABBIT_HOLE:
                return (row_index, column_index)

def get_commands():
    directions = {"right": [0, 1],
              "left": [0, -1],
              "up": [-1, 0],
              "down": [1, 0]
              }
    return directions


def is_valid(player_row, player_col):
    if 0 <= player_row < len(matrix) and 0 <= player_col < len(matrix):
        return True
    return False


def play_game():
    command = input()
    bags_of_tea = 0
    matrix[alice_row][alice_column] = "*"
    row = alice_row
    column = alice_column
    while True:
        command_row, command_col = side[command]
        row += command_row
        column += command_col
        if is_valid(row, column):
            if matrix[row][column] == RABBIT_HOLE:
                matrix[row][column] = "*"
                print("Alice didn't make it to the tea party.")
                for row in matrix:
                    print(" ".join([str(x) for x in row]))
                break


            elif type(matrix[row][column]) == int:
                bags_of_tea += matrix[row][column]
                matrix[row][column] = "*"
                if bags_of_tea >= 10:
                    print("She did it! She went to the party.")
                    for row in matrix:
                        print(" ".join([str(x) for x in row]))
                    break
            else:
                matrix[row][column] = "*"
        else:
            print("Alice didn't make it to the tea party.")
            for row in matrix:
                print(" ".join([str(x) for x in row]))
            break


        command = input()


matrix = read_matrix()
alice_row, alice_column = find_alice_position(matrix)
rabbit_hole_row, rabbit_hole_column = find_rabbit_hole_position(matrix)
side = get_commands()
play_game()
