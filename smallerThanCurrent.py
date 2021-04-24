array = [6,5,4,8]
a=[]

for i in range(len(array)):
    count = 0
    for j in range(len(array)):
        if array[i] > array[j] and i!=j:
            count = count+1
    a.append(count)

print(a)
