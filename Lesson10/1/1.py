# Вариант 7

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

def ReturnMatrix(matrix: []):
    New_matrix = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                matrix[i][j] = matrix[i-1][j]
            New_matrix.append(matrix[i][j])
    return New_matrix



matrix = InputFileMatrix('input.txt')

New_matrix = str(ReturnMatrix(matrix))

OutputFile('output.txt', New_matrix)
