rows = int(input())

def matr():
  matrix = []
  for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    even_row = [el for el in row if el % 2 == 0]
    matrix.append(even_row)
  return matrix
matrix = matr()

print(matrix)