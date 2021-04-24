



def add(myList):
    newList = []
    for i in range(len(myList)):
        if i == 0:
            newList.append(myList[i])
        else:
            newList.append(myList[i]+newList[i-1])

    return newList

list = [1,2,3,4,5]
val = add(list)
print(val)