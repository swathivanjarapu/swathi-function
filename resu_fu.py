def table(n,i):
  print (n*i)
  i=i+1
  if i<=10:
    table(n,i)
table(12,1)

def recursive_list_sum(data_list):
    total = 0
    for element in data_list:
        if type(element) == type([]):
            total = total + recursive_list_sum(element)
        else:
            total = total + element

    return total
print( recursive_list_sum([1, 2, [3,4],[5,6]]))