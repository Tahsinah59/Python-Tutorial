"""
Created on Tue Aug 15 10:28:49 2023
@author: Tahsinah Banu
"""

#Higher order function

def greet(func):
    func()
    
def greet2():
    def func():
        return 5
    return func




