def maxSum(matrix):
    greatestValue = 0
    list = []
    for i in range(len(matrix)):
        cust = sum(matrix[i])
        list.append(cust)
    return max(list)
matrix = [[1,6],[2,9],[3,4]]
valu = maxSum(matrix)
print(valu)