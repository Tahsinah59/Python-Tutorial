"""
Created on Mon Aug 14 12:32:32 2023
@author:Tahsinah Banu
"""
# 1. lambda square function 
# 2. list sort with rwspect to tuples 2nd value

my_list = [3,4,5]

print(list(map(lambda item : item**2, my_list)))
print(my_list)

a = [(0,2), (4,3), (10, -1), (9,9)]

a.sort(key= lambda x: x[1])
print(a)


