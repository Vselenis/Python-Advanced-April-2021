def get_magic_triangle(n):
    magic_triangle = []
    for i in range(1, n+1):
        if i == 1:
            magic_triangle.append([1])
        elif i == 2:
            magic_triangle.append([1, 1])
        else:
            new_row = []
            new_row.append(1)
            for x in range(i-2):
                zz = magic_triangle[len(magic_triangle) - 1][x] + magic_triangle[len(magic_triangle) - 1][x+1]
                new_row.append(zz)
            new_row.append(1)
            magic_triangle.append(new_row)

    return magic_triangle

n = 5
get_magic_triangle(n)