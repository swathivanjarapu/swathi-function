def fun(l):
    i=0
    m=[0]
    while i<len(l):
        if l[i]>m:
            m=l[i]
        i=i+1
    return m
d=fun([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])
print((len(d),d))


def fun(l):
    i=0
    m=[0]
    while i<len(l):
        if l[i]<m:
            m=l[i]
        i=i+1
    return m
d=fun([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])
print((len(d),d))

    
    
   