# def max_n(a):
#     b=max(a)
#     print(b)
# max_n([1,3,5,6,7,8])


def fun(a):
    i=0
    b=a[i+1]-a[i]
    while i<=len(a)-2:
        c=a[i+1]-a[i]
        if b==c:
            print("true")
        
        else:
            print("false")
        i=i+1
print(fun([45,46,47,48,49,51,52]))
