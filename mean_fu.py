# def menu(day):
#     if day == "monday":
#         return "Butter Chicken"
#     elif day == "tuesday":
#         return "Mutton Chaap"
#     else:
#         return "Chole Bhature"

#     print ("Kya main print ho payungi? :-(")

# mon_menu = menu("monday")
# print (mon_menu)
# tues_menu = menu("tuesday")
# print (tues_menu)
# fri_menu = menu("friday")
# print (fri_menu)

import random

sa= ['A', 'B', 'C', 'D', 'E',['1','3','4']]
i=0
c=[]
while i<len(sa):
    j=0
    while j<len(sa):
        d=sa[i]+sa[j]
        j=j+1
        c.append(d)
    i=i+1
print(c)
random.shuffle(c)
random.shuffle(c)
print(c)