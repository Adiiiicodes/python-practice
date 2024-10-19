def matt(x, y, mat):
    tmat = [[0 for _ in range(x)] for _ in range(y)]

    for k in range(x):
        for l in range(y):
            tmat[l][k] = mat[k][l]
    return tmat


def reverse_rows(matrix):
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
    return matrix


def matr():
    transposed_matrix = matt(r, c, mat)
    rotated_matrix = reverse_rows(transposed_matrix)

    print('The rotated Matrix by 90 degrees is:')
    for row in rotated_matrix:
        print(row)


r = int(input('The number of rows in the matrix: '))
c = int(input('The number of columns in the matrix: '))

mat = [[0 for _ in range(c)] for _ in range(r)]
for i in range(r):
    for j in range(c):
        mat[i][j] = int(input(f'Enter the number at index {i}, {j}: '))

print('The original Matrix is:')
for row in mat:
    print(row)

matr()
