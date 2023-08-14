"""
Created on Mon Aug 14 12:14:29 2023
@author: Tahsinah Banu
"""

# lambda param: actions(param)
from functools import reduce
my_list = [1,2,3]

print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: item%2!=0, my_list)))
print(reduce(lambda acc, item: acc+item, my_list, 0))
print(my_list)