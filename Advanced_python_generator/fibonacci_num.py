"""
Created on Sun Aug 20 22:02:56 2023
@author: Tahsinah Banu
"""

def fib(number):
    a=0
    b=1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b
        
        
for x in fib(21):
    print(x)