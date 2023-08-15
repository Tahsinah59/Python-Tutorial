"""
Created on Tue Aug 15 11:24:36 2023
@author: Tahsinah Banu
"""

# Use of decorator

from time import time

def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i*5
        
        
long_time()