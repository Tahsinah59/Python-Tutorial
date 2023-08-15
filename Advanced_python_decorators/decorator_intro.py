"""
Created on Tue Aug 15 10:24:26 2023
@author: Tahsinah Banu
"""

def hello(func):
    func()
    
def greet():
    print('Still here!')
    
a = hello(greet)

print(a)