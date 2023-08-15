"""
Created on Tue Aug 15 10:33:13 2023
@author: Tahsinah Banu
"""
#Decorator


def my_decorator(func):
    def wrap_func():
        print('***********')
        func()
        print('***********')
    return wrap_func


@my_decorator 
def hello():
    print('helllooooo')
        
@my_decorator         
def bye(): 
    print('see ya letter')  
    
    
    
hello()
bye()