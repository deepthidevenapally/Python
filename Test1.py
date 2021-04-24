
def options(jeans,shoes,skirts,tops,dollars):
    comb = []
    for (jean,shoe,skirt,top) in zip(jeans,shoes,skirts,tops):
        items = []
        continueFlag = []
        items.append((shoe))
        diff = dollars - shoe
        if(diff>0 and diff-jean>0):
            diff = diff-jean
            continueFlag.append(True)
        else:
            break
        if(diff>0 and diff-skirt>0 and len(continueFlag)==1):
            diff=diff-skirt
            items.append((skirt))
            continueFlag.append(True)
        else:
            break
        if(diff>0 and diff-top>0 and len(continueFlag)==2):
            diff=diff-top
            items.append((top))
        comb.append(items)
    return len(comb)




print(options([2,3],[5],[2,3],[1,2],20))