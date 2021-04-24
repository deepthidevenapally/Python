
def palin(num):
    mylist = [x for x in str(num)]
    for i,_ in enumerate(mylist):
        if mylist[i] == mylist[len(mylist)-i-1]:
            return True
        else:
            return False
print(palin("abba"))



