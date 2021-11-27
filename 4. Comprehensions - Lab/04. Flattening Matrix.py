def read_matrix():
  rows = int(input())
  return [input().split(", ") for _ in range(rows)]

matrix = read_matrix()
print([int(x) for row in matrix for x in row])