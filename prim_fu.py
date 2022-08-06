# def pri(a):
#     i=2
#     j=0
#     while i<a//2:
#         if a%i==0:
#             j=1
#             break
#         i=i+1
#     if j==0:
#         print("prime")
#     else:
#         print("not")
# pri(int(input("enter number")))


def is_prime(num):
   if num <= 1:
      return False
   for i in range(2, num):
      if num % i == 0:
         return False
   return num
def solve(num):
   if not is_prime(num):
      return False
   reverse_num = 0
   l=[]
   while num != 0:
      d = num % 10
      reverse_num = reverse_num * 10 + d
      num = int(num / 10)

   return is_prime(reverse_num)
n = int(input("enter number"))
print (solve(n))
    
            