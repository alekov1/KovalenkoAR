# Вариант 7


def ReturnMatrix(matrix: []):
    New_matrix = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                matrix[i][j] = matrix[i-1][j]
            New_matrix.append(matrix[i][j])
    return New_matrix


matrix = [[1, 5, 7],
          [0, 5, 0],
          [0, 0, 0]]

New_matrix = ReturnMatrix(matrix)
