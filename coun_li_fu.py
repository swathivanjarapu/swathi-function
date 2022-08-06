# def coun(a):
#     c=0
#     i=0
#     while i<len(a):
#         c=c+1
#         i=i+1
#     return c
# d=coun([1,2,3,4,5,6,7,8])
# print(d)

def coun(a):
    c=0
    i=0
    while i<len(a):
        if a[i]%2==0:
            c=c+1
        i=i+1
    return c
d=coun([1,2,3,4,5,6,7,8])
print(d)
    
    
