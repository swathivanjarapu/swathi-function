def li(n):
    i=0
    ma=0
    sec=n[0]
    while i <len(n):
        if n[i]>ma:
            ma=n[i]
        elif ma>n[i] and n[i]>sec:
            sec=n[i]
        i=i+1
    print(ma)
    print(sec)
li([2,5,7,8,9,10,12])