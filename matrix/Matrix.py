import copy

def InputMatrix(titleSize,titleInput):

    print()
    matrix= []
    try:
        size = input(titleSize).split(' ')
        size[0] = int(size[0])
        size[1] = int(size[1])
        print()
        print(titleInput)
    
        for i in range(size[0]):
            a = []
            line = input().split(" ")
            for j in range(size[1]):
                a.append(int(line[j]))
            matrix.append(a)
    except:
        print("Ошибочные данные")
        raise SystemExit
       
    

    return matrix
def PrintMatrix(matrix,title):
    print()
    print(title)
    for i in range(len(matrix)):
        a = ""
        for j in range(len(matrix[i])):
            a = a + str(matrix[i][j])+ " "
        print(a)

def AddMatrices(m1,m2):
    matrix=copy.copy(m1)

    for i in range(len(matrixFirst)):
        for j in range(len(matrixFirst[0])):
            matrix[i][j] = m1[i][j] + m2[i][j]

    PrintMatrix(matrix,"The result add matrix")
    return matrix
def MultiplyMatricesByConst(m):
    constant = float(input("Enter constant: "))
    matrix = copy.copy(m)

    for i in range(len(m)):
        for j in range(len(m[0])):
            matrix[i][j] = m[i][j] * constant

    PrintMatrix(matrix, "Multiply matrices by a constant")
def MultiplyMatrices(a,b):
     zip_b = zip(*b)
     zip_b = list(zip_b)
     PrintMatrix( [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))for col_b in zip_b] for row_a in a], "Multiply matrix:")
def Transpose(m,_type):
    if _type == "main":
        PrintMatrix([[m[j][i] for j in range(len(m))] for i in range(len(m[0]))], "Transpose matrix") 
    if _type == "second":
        matrix = m
        row = len(m)
        col = len(m[0])
        for i in range(1, row - 1):
            for j in range(col - i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[row - j][row - i]
                matrix[row - j][row-i] = temp
        PrintMatrix(matrix, "Second diagonal")



def det2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
def minor(matrix, i, j):
    tmp = [row for k, row in enumerate(matrix) if k != i]
    tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
    return tmp
def Determinant(matrix):
    size = len(matrix)
    if size == 2:
        return det2(matrix)
    print("determinant: " + str(sum((-1) ** j * matrix[0][j] * Determinant(minor(matrix, 0, j)) for j in range(size)))) 

def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]
def gauss(a):
    try:
        for i in range(len(a)):
            if a[i][i] == 0:
                for j in range(i+1, len(a)):
                    if a[i][j] != 0:
                            a[i], a[j] = a[j], a[i]
                            break
                    else:
                        print("-")
                for j in range(i+1, len(a)):
                    eliminate(a[i], a[j], i)
            for i in range(len(a)-1, -1, -1):
                for j in range(i-1, -1, -1):
                    eliminate(a[i], a[j], i)
            for i in range(len(a)):
                eliminate(a[i], a[i], i, target=1)
            return a
    except:
        print("Неверные данные деление на ноль")
        raise SystemExit
   
def Inverse(a):
    tmp = [[] for _ in a]
    for i,row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    PrintMatrix(ret, "Invers matrix")





work = True
while(work):
    print("""
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit 
""")

    CHOICE = input("Your choice:")

    if CHOICE == "1":

        matrixFirst = InputMatrix("Enter size of first matrix: ","Enter first matrix: ")
        matrixSecond = InputMatrix("Enter size of second matrix: ","Enter second matrix: ")

        if len(matrixFirst) == len(matrixSecond) and len(matrixFirst[0]) == len(matrixSecond[0]):
            AddMatrices(matrixFirst, matrixSecond)
        else:
            print("Размер матриц должен быть одинаковый")
    if CHOICE == '2':
        matrix = InputMatrix("Enter size of matrix: ", "Enter matrix ")
        MultiplyMatricesByConst(matrix)
    if CHOICE == '3':
        matrixFirst = InputMatrix("Enter size of first matrix: ", "Enter first matrix")
        matrixSecond = InputMatrix("Enter size of second matrix: ", "Enter second matrix")
        if len(matrixFirst) == len(matrixSecond[0]):
            MultiplyMatrices(matrixFirst, matrixSecond)
        else:
            print("Чтобы можно было умножить две матрицы, количество столбцов первой матрицы должно быть равно количеству строк второй матрицы.")
    if CHOICE == '4':
        tranType = input("""
        1. Main diagonal
        2. Side diagonal
        3. Vertical line
        4. Horizontal line
        """)

        matrix = InputMatrix("Enter size of matrix: ", "Enter matrix ")

        if tranType == '1':
            Transpose(matrix,"main")
        if tranType == '2':
            print("2")
        if tranType == '3':
            print("3")
        if tranType == '4':
            print("4")   
    if CHOICE == '5':
        matrix = InputMatrix("Enter size of matrix: ", "Enter matrix")
        Determinant(matrix)
    if CHOICE == '6':
        matrix = InputMatrix("Enter size of matrix: ", "Enter matrix")
        Inverse(matrix)
    if CHOICE == "0":
        work = False

