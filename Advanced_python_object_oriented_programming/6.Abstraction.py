"""
Created on Mon Jul 31 11:02:37 2023
@author: Tahsinah Banu
"""

class Playercharacters:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def run(self):
        print('run')
        
    def shout(self):
        print(f'My name is {self.name} and age is {self.age}')
        
        
player1 = Playercharacters('Andrei', 44)

player1.name = '!!!'
player1.age = 32
player1.shout='boo'

print(player1.name)
print(player1.shout)
print(player1.age)

'''
Note:
    
    Abstraction means keeping class attribute and methods aside from the outsider
    to modify them. But in python there is no process of public and private. There 
    is only naming convention that indicates that one should not modify the 
    attributes and method while seeing the naming convension.
    
'''