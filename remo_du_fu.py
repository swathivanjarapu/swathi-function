def li(a):
    i=0
    c=[]
    while i<len(a):
        if a[i] not in c:
            c.append(a[i])
        i=i+1
    print(c)
li([1,2,3,3,3,3,4,5])
