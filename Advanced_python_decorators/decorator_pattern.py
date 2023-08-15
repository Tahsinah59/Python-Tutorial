"""
Created on Tue Aug 15 11:07:01 2023
@author: Tahsinah Banu
"""

# Decorator pattern

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrap_func
        

@my_decorator
def hello(greeting, emoji=':)'):
    print(greeting, emoji)       
    
hello('hiiii')