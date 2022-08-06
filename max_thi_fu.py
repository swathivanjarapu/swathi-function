def fun(a,b,c):
    if a>b:
        if a>c:
            print(a,"largest")
        else:
            print(c,"is largest")
    else:
        if b>c:
            print(b,"largest")
        else:
            print(c,"largest")
a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
fun(a,b,c)