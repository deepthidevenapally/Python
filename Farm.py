# We want to count the number of fields on a farm divided into a rectangular grid of square-shaped cells.
# Every cell either has grass on it or is empty. If cells with grass share an edge, they belong to a common field.
# Create a function which takes in the rectangular grid as a 2 dimensional array containing boolean values,
# with True values representing grass and False values representing no-grass. The function should return the number of fields.

def checkField(arr):
    fields = 0
    for i in arr:
        flag = False
        for j in i:
            if i.index(j)<len(i) and j==True and i[i.index(j) + 1]==True:
                flag = True
        if flag:
            fields = fields + 1
        else:
            fields = fields + 0
    return fields

print(checkField([[True,False,False],[True,False,False],[True,True,True]]))