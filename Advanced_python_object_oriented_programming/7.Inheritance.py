# Inheritance
"""Created on Tue Aug  1 08:42:06 2023
@author: Tahsinah Banu
"""

class user():
    def sign_in(self):
        print('Logged in')
        
class Wizard(user):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        
    def attack(self):
        print(f'attacking with power with {self.power}')
        
class Archer(user):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
        
    def attack(self):
        print(f'attacking with arrows: arrows left-{self.num_arrows}')
        
        
wizard1 = Wizard('Marline', 50)
archer1 = Archer('Robin', 400)
wizard1.attack()
archer1.attack()
archer1.sign_in()

print(isinstance(wizard1,user))
print(isinstance(wizard1,object))
print(isinstance(user,object))





        

