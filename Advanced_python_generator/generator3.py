"""
Created on Sun Aug 20 20:47:27 2023
@author: Tahsinah Banu
"""

def gen_fun(num):
    for i in range(num):
        yield i
        
        
for item in gen_fun(100):
    print(item)