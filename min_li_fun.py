def min_li(a):
    i=0
    min=a[0]
    while i<len(a):
        if a[i]<min:
            min=a[i]
        i=i+1
    print(min)
min_li([2,4,6,7,8,9])