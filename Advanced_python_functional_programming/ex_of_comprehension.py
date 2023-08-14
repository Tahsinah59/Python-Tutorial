"""
Created on Mon Aug 14 13:33:56 2023
@author: Tahsinah Banu
"""
# Excersise of comprehensions : create a list that does not contain duplicates.

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

my_comp = list(set([x for x in some_list if some_list.count(x)>1]))
print(my_comp)
