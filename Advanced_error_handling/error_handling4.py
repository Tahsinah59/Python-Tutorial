"""
Created on Tue Aug 15 14:58:09 2023
@author: Tahsinah Banu
"""
# Error handling 4

while True:
    try:
        age = int(input('what is your age?'))
        10/age
        raise Exception('hey! Cut it out!')
    except ZeroDivisionError:
        print('please enter age higher than 0')
        continue
    else:
        print(age)
        print('Thank you!')
    finally:
        print('OK! I am done')
    print('can you hear me!')
