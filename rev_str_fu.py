# def rev(l):
#  "1234abcd"


# def sumDigits(no):
#     return 0 if no == 0 else int(no % 10) + sumDigits(int(no/10))


# # Driver code
# print(sumDigits(687))

# def multiply_list(items):
#     tot = 1
#     for x in items:
#         tot *= x
#     return tot

# print(repr(4+2))

def sumDigits(n):
    i=0
    while i<len(n):
        if n[-i] == 0:
           n. remove(0)
           i=i+1
    return n
        
        
c=sumDigits(input("enter number"))
print(c)


