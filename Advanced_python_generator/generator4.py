"""
Created on Sun Aug 20 20:52:53 2023
@author: Tahsinah Banu
"""

def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator)*2)
        except StopIteration:
            break
        
special_for([1,2,3])