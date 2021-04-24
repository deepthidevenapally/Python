def comb(arr_old, n):
    arr_new3 = []
    arr_new1 = arr_old[:len(arr_old)-n]
    arr_new2 = arr_old[len(arr_old)-n:]
    for i,j in zip(arr_new1,arr_new2):
        arr_new3.append(i)
        arr_new3.append(j)
    return arr_new3

val = comb([1,2,3,4],2)
print(val)