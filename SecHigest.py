def secHigest(list):
    list.remove(max(list))
    return max(list)

print(secHigest([1,2,5,9]))