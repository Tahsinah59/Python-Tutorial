"""
Created on Mon Jul 31 10:23:49 2023
@author: Tahsinah Banu
"""

class PlayerCharacters:
    membership = True    # Class object attribute
    
    def __init__(self,name, age):
        if(self.membership):
            self.name = name
            self.age = age
            
    def shout(self):
        print(f'my name is {self.name} ')
        
player1 = PlayerCharacters('Cindy', 20)
player2 = PlayerCharacters('Tom', 30)


print(player1.membership)
print(player2.membership)

print(player1.shout())
print(player2.shout())

