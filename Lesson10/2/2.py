def InputFileMatrix(file: str):
    FileMatrix = open(file).readlines()
    Matrix = []
    for i in FileMatrix:
        spisok = []
        for j in i.split():
            spisok.append(int(j))
        Matrix.append(spisok)
    return Matrix

def OutputFile(file: str, result: str):
    FileMatrix = open(file, mode='w')
    FileMatrix.write(result)
    FileMatrix.close()

def DiagonalArrayOfMatrix(matrix: [], n: int):
    DiagonalMatrix = []
    for i in range(0, n):
        for j in range(0, n):
            if (i == j):
                DiagonalMatrix.append(matrix[i][j])
            if ((i + j) == (n - 1)):
                DiagonalMatrix.append(matrix[i][j])
    return DiagonalMatrix

def SumDiagonalofMatrix(matrix: [], n: int):
    SumDiagonalMatrix = 0

    for i in range(0, n):
        for j in range(0, n):
            if (i == j):
                SumDiagonalMatrix += matrix[i][j]
    return SumDiagonalMatrix


def TransformMatrix(matrix, n):

    trace = SumDiagonalofMatrix(matrix, n)
    TransformedMatrix = matrix.copy()
    for i in range(0, n):
        if i % 2 == 0:
            for j in range(0, n):
                TransformedMatrix[i][j] = matrix[i][j] // trace
    return TransformedMatrix


matrix = InputFileMatrix('input.txt')
n = 3

if DiagonalArrayOfMatrix(matrix, n) and SumDiagonalofMatrix(matrix, n) and TransformMatrix(matrix, n):
    MM, MS, MA = DiagonalArrayOfMatrix(matrix, n), SumDiagonalofMatrix(matrix, n), TransformMatrix(matrix, n)
    OutputFile('output.txt', f"{str(MM)} Одномерный массив из диагоналей матрицы \n {str(MS)} След матрицы \n {str(MA)} Измененная матрица")


