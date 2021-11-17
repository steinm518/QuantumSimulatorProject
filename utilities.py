import math
Matrix = list[list[float]]
def zeroes(x:int,y:int):
    mat:Matrix=[]
    for i in range(x):
        row:list[float]=[]
        for j in range(y):
            row.append(0)
        mat.append(row)
    return mat

def matmul(mat1:Matrix, mat2:Matrix):
    mat3=[]
    mat2=transpose(mat2)
    for row in mat1:
        curRow=[]
        for col in mat2: 
             curRow.append(sum(row*col))
        mat3.append(curRow)
    return mat3

def transpose(mat1:Matrix):
    mat2=[]
    for x in range(len(mat1[0])):
        curRow=[]
        for y in range(len(mat1)):
            curRow.append(None)
        mat2.append(curRow)
    for x in range(len(mat1)):
        for y in range(len(mat1[0])):
            mat2[y][x]=mat1[x][y]
    return mat2

def tensor(mat1:Matrix,mat2:Matrix):
    tensorSize = (len(mat1)*len(mat2),len(mat2[0])*len(mat1[0]))
    print(tensorSize)
    mat3=[]
    for row1 in mat1:
        for col2 in mat2:
            curRow=[]
            for x in row1:
                curRow.extend((scale([col2],x)[0]))
            mat3.append(curRow)
    return mat3
def scale(mat1:Matrix,num:int):
    mat2 = zeroes(len(mat1),len(mat1[0]))
    for x in range(len(mat1)):
        for y in range(len(mat1[0])):
            mat2[x][y]=num*mat1[x][y]
    return mat2