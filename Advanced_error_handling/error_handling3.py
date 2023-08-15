"""
Created on Tue Aug 15 14:32:55 2023
@author: Tahsinah Banu
"""
# error handling 3

while True:
    try:
        age = int(input('what is your age?'))
        10/age
    except ValueError:
        print('Please enter a number')
        continue
    except ZeroDivisionError:
        print('please enter age higher than 0')
        continue
    else:
        print(age)
        print('Thank you!')
        break
    finally:
        print('OK! I am done')
    print('can you hear me!')