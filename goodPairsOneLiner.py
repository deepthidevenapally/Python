array = [1,2,3,1,1,3]
a = [(i,j) for i in range(len(array)) for j in range(i+1,len(array)) if array[i] == array[j] and i<j]
print(len(a))