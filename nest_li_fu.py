def mac(n):
    i=0
    a=[]
    while i<len(n):
        j=0
        max=0
        while j<len(n[i]):
            if n[i][j]>max:
                max=n[i][j]
            j=j+1
        a.append(max)
        i=i+1
    print(a)
mac([[3,5,6,7],[7,9,12,15,28],[6,78,90,98],[9,78,67,56,65],[78,56,45,34,100,200]])
        