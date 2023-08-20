"""
Created on Sun Aug 20 19:12:00 2023
@author: Tahsinah Banu
"""

# general way to create generator

def generator_function(num):
    for i in range(num):
        yield i*2


#for item in generator_function(1000):
    #print(item)
    

g = generator_function(100)
next(g)
next(g)
print(next(g))