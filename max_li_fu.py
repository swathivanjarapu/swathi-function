def add_two_li(a):
    i=0
    c=[]
    m=a[0]
    while i<len(a):
        if a[i]>m:
            m=a[i]
        i=i+1
    print(m)
add_two_li([1,2,3,4,5])
