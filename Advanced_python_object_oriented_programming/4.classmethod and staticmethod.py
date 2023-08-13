"""
Created on Wed Aug  2 04:07:45 2023
@author: Tahsinah Banu
"""
#@classmethood and @ staticmethod

class PlayerChatacter:
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def shout(self):
        print(f'my name is {self.name}')
        
    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Tomy', num1+num2)
    
    @staticmethod
    def adding_things2(num1, num2):
        return num1+num2
    
player1 = PlayerChatacter('Tom', 44)
    
print(player1.adding_things(2, 3))

print(PlayerChatacter.adding_things(2,3))

player3 = PlayerChatacter.adding_things(2,3)      
print(player3.age)


print(player1.adding_things2(2, 3))
