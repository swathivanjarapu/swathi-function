# def add_numbers(number_x, number_y):
#     number_sum = number_x + number_y
#     return number_sum

# sum1 = add_numbers(20, 40)
# print (sum1)
# sum2 = add_numbers(560, 23)
# a = 1234
# b = 12
# sum3 = add_numbers(a, b)
# print (sum2)
# print (sum3)
# number_a = add_numbers(20, 40) / add_numbers(5, 1)
# print (number_a)


# def eradicate(n):
#     n_as_str = str(n)
#     if n_as_str == "0":
#         return 0
#     if n_as_str[-1] == "0":
#         return eradicate(int(n_as_str[:-1]))
#     else:
#         return n


# print(eradicate(1050))

# def fun():
#     i=1
#     a=[]
#     while i <=10:
#         a.append(i)
#         i=i+1
#     return a
# def fun1():
#     b=fun()
#     j=0
#     c=[]
#     while j<len(b):
#         c.append(b[:3])
#         c.append(b[-1:-4:-1])
#         j=j+10
#     print(c)
# fun1()

def fun(a):
    i=0
    b=[]
    s=0
    while i<len(a):
        j=0
        while j<len(a[i]):
            b.append(a[i][j])
            j=j+1
        i=i+1
    
    print([b])
    
a=[['a','b'],['b','c','d'],['e','f']]
fun(a)
