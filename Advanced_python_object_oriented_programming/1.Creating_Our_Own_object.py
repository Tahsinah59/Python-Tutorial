"""
Created on Mon Jul 31 09:54:21 2023
@author: Tahsinah Banu
"""

class PlayerCharacters:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def run(self):
        print(f'I am {self.name} and {self.age} years old')
        
        
player1 = PlayerCharacters('Cindy', 21)  
player2 = PlayerCharacters('Tom', 40)


print(player1.name)
print(player2.run())
