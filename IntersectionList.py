def intersect(l1,l2):

    final = []
    for i in l1:
        if i in l2:
            final.append(i)
    return final

print(intersect([1,2,3,8,5],[3,5,6,8]))
