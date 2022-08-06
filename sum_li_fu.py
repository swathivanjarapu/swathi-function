# def add_two_li(a,b):
#     i=0
#     c=[]
#     while i<len(a):
#         d=a[i]+b[i]
#         c.append(d)
#         i=i+1
#     print(c)
# add_two_li([1,2,3],[3,4,5])

# def even_li(a):
#     i=0
#     b=[]
#     while i<len(a):
#         if a[i]%2==0:
#             b.append(a[i])
#         i=i+1
#     print(b)
# even_li([1,2,4,5,6,7,8,9,10])

def even_li(a):
    i=0
    b=[]
    s=a[0]
    while i<len(a):
        if a[i]%2==0:
            s=s+a[i]
            b.append(a[i])
        i=i+1
    print(b)
    print(s)
even_li([1,2,4,5,6,7,8,9,10])

