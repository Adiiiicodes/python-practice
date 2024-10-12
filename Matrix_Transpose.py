def matt(x,y,mat):
    tmat = [[0 for _ in range(x)] for _ in range(y)]
    for k in range(x):
        for l in range(y):
            tmat[k][l]=mat[l][k]
    print('the transpose matrix is : ')
    for el in tmat:
        print(el)
x=int(input('Enter the number of rows required : '))
y=int(input('Enter the number of coloumns required : '))
mat=[]
for i in range(x):
    colmat=[]
    for j in range(y):
        ele=int(input(f'Enter the element at index ({i}) , ({j}) : '))
        colmat.append(ele)
    mat.append(colmat)
print('The original matrix is : ')
for colmat in mat:
    print(colmat)
matt(x,y,mat)