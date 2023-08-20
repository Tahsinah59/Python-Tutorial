"""
Created on Sun Aug 20 19:04:44 2023
@author: Tahsinah Banu
"""

def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

my_list = make_list(100)
#print(list(range(1000000)))