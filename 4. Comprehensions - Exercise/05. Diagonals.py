# def read_matrix():
#     matrix = []
#     rows = int(input())
#     for _ in range(rows):
#         matrix.append([int(num) for num in input().split(", ")])
#     return matrix

matrix = [[int(num) for num in input().split(", ")]for _ in range(int(input()))]
[print(f'{key}: {", ".join([str(x) for x in value])}. Sum: {sum(int(x) for x in value)}') for dictionary in [{"First diagonal" : [matrix[i][i] for i in range(len(matrix))]}, {"Second diagonal" : [matrix[i][len(matrix) - i - 1] for i in range(len(matrix))]}] for key, value in dictionary.items()]