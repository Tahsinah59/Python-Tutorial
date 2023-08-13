
"""
Created on Mon Jul 31 10:37:28 2023
@author: Tahsinah Banu
power of __init__
"""

class PlayerCharacters:
    membership = True
    
    def __init__(self, name= 'anonymous', age=20):
        if(age>18):
            self.name = name
            self.age = age
            
    def shout(self):
        print(f'my name is {self.name} and age is {self.age}')
        
        
player1 = PlayerCharacters()
player2 = PlayerCharacters('Cindy', 19)
player3 = PlayerCharacters('Tom', 17)

print(player1.shout())
print(player2.shout())
print(player3.shout())