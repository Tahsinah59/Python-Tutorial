"""
Created on Tue Aug 15 12:01:25 2023
@author: Tahsinah Banu
"""

#error handling 1

while True:
    try:
        age = int(input('what is your age?'))
        10/age
    except ValueError:
        print('Please enter a number')
   
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print(age)
        print('Thank you!')
        break