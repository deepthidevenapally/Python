def matrixSum(matrix):
    rowLen = len(matrix)
    colLen = len(matrix[0])
    total = 0
    for i in range(rowLen):
        for j in range(colLen):
            if i == j or i+j == rowLen-1:
                total += matrix[i][j]
    return total

print(matrixSum([
    [1,2,3],
    [4,5,6],
    [7,8,9]]))

