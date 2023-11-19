
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


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
n = 3

MD = DiagonalArrayOfMatrix(matrix, n)
print(f"{MD} Одномерный массив из диагоналей матрицы ")
MS = SumDiagonalofMatrix(matrix, n)
print(f"{MS} След матрицы")
MA = TransformMatrix(matrix, n)
print(MA)