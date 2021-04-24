def topK(myList,k):
    temp_dict = {}
    temp_dict2 = {}
    tempTopKeys = []

    for ele in set(myList):
        temp_dict[myList.count(ele)] = ele
    keys = temp_dict.keys()
    keys.sort()
    for i in range(len(keys), k):
        for j in range(keys):
            temp_dict2[key]
            tempTopKeys.append()





print(topK([1,1,1,1,2,2,3]))

