def matm():
    matA= [[0 for _ in range(ca)] for _ in range(ra)]
    matB= [[0 for _ in range(cb)] for _ in range(rb)]

    for i in range(ra):
        for j in range(ca):
            matA[i][j]=int(input(f'Enter the element for Matrix A at index {i} {j} : '))


    for k in range(rb):
        for l in range(cb):
            matB[k][l]=int(input(f'Enter the element for Matrix B at index {k} {l} : '))
    print('Matrix A')
    for row in matA:
        print(row)
    print('Matrix ')
    for row in matB:
        print(row)

    res = [[0 for _ in range(cb)] for _ in range(ra)]

    for a in range(ra):
        for b in range(cb):
            for c in range(ca):
                res[a][b] += matA[a][c]*matB[c][a]
    print('Result Matrix ')
    for row in res:
        print(row)

while True :
    ra = int(input('Enter the number of rows in matrix A : '))
    ca = int(input('Enter the number of coloumns in matrix A : '))
    rb = int(input('Enter the number of rows in matrix B : '))
    cb = int(input('Enter the number of coloumns in matrix B : '))

    if ca == rb:
        matm()
        break
    else:
        print('Invalid Matrices')
        print('The number of coloumns in matrix A should be equal to the number of rows in matrix B')