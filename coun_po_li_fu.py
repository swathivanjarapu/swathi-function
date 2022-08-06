def coun(l):
    i=0
    c=0
    a=0
    while i<len(l):
        if l[i]>0:
            c=c+1
        else:
            a=a+1
        i=i+1
    print(c)
    print(a)
coun([2, -7, 5, -64, -14])

