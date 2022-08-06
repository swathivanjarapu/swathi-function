def fun(a):
    i=1
    b=[]
    while i<=a:
        b.append(i)
        i=i+1
    return b
        
def fun1():
    a=int(input("enter number"))
    print(fun(a))
fun1()

def fun():
    i=1
    a=[]
    while i<=10:
        a.append(i)
        i=i+1
    return a
def fun1():
    b=fun()
    j=0
    d=[]
    c=[]
    while j<len(b):
        if b[j]%2==0:
            c.append(b[j])
        else:
            d.append(b[j])
        j=j+1
    return c ,d
print(fun1())
            
    