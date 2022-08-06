def per(n):
    i=1
    sum=0
    while i<n:
        if n%i==0:
            sum=sum+i
        i=i+1
    return sum
n=int(input("enter number"))
s=per(n)
if n==s:
    print("per")
else:
    print("not")