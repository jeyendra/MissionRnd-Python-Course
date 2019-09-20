def get_hcf(l1,l2):
    i,j=0,0
    res=[]
    while  i<len(l1) and j<len(l2):
        if l1[i][0]==l2[j][0]:
            res.append((l1[i][0],min(l1[i][1],l2[j][1])))
            i+=1
            j+=1
        elif l1[i][0]<l2[j][0]:
            i+=1
        else:
            j+=1
    return res
def get_lcm(l1,l2):
    i,j=0,0
    res=[]
    while((i<len(l1))and(j<len(l2))):
        if l1[i][0]==l2[j][0]:
            res.append((l1[i][0],max(l1[i][1],l2[j][1])))
            i+=1
            j+=1
        elif l1[i][0]<l2[j][0]:
            res.append(l1[i])
            i+=1
        else:
            res.append(l2[j])
            j+=1
    while i<len(l1):
        res.append(l1[i])
        i+=1
    while j<len(l2):
        res.append(l2[j])
        j+=1
    return res
def multiply(l1,l2):
    i,j=0,0
    res=[]
    while((i<len(l1))and(j<len(l2))):
        if l1[i][0]==l2[j][0]:
            res.append((l1[i][0],l1[i][1]+l2[j][1]))
            i+=1
            j+=1
        elif l1[i][0]<l2[j][0]:
            res.append(l1[i])
            i+=1
        else:
            res.append(l2[j])
            j+=1
    while i<len(l1):
        res.append(l1[i])
        i+=1
    while j<len(l2):
        res.append(l2[j])
        j+=1
    return res