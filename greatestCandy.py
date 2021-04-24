def candyGame(array,n):
    max_val = max(array)
    print(max_val)
    booleanList = []
    for i in array:
        if i+n< max_val:
            booleanList.append(False)
        else:
            booleanList.append(True)
    return booleanList

val = candyGame([1,2,3,4,5],3)
print(val)