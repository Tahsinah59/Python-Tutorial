"""
Created on Mon Jul 31 10:47:49 2023
@author: LENOVO
"""

class PlayerCharacters:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def run(self):
        print('run')
        
    def shout(self):
        print(f'My name is {self.name} and age is {self.age}')
        
player1 = PlayerCharacters('Tom',23)

print(player1.shout())
print(player1.run())
print(player1.name)
print(player1.age)

# Encapsulation: packaged up together