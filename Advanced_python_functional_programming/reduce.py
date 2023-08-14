"""
Created on Mon Aug 14 11:54:21 2023
@author: Tahsinah Banu
"""
#reduce

from functools import reduce


my_list = [1,2,3]

def accumulator(acc,item):
    print(acc,item)
    return acc+item

print(reduce(accumulator, my_list, 0))
print(my_list)
