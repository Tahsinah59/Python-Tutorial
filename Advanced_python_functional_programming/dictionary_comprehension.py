"""
Created on Mon Aug 14 12:59:12 2023
@author: LENOVO
"""

simple_dict = {
        'a' : 1,
        'b' : 2,
        'c' : 3
    }

my_dict2 = {k: v**2 for k,v in simple_dict.items() if v%2 != 0}
my_dict = {num:num*2 for num in [1,2,3] }

print(my_dict2)
print(my_dict)