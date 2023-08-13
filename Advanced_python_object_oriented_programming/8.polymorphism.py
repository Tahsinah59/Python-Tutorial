"""
Created on Tue Aug  1 18:22:41 2023
@author: Tahsinah Banu
"""

# Polymorphism


class user():
    def sign_in(self):
        print('Logged in')
        
    def attack(self):
        print("do nothing")
        
class Wizard(user):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        
    def attack(self):
        user.attack(self)
        print(f'attacking with power with {self.power}')
        
class Archer(user):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
        
    def attack(self):
        user.attack(self)
        print(f'attacking with arrows: arrows left-{self.num_arrows}')
        
        
wizard1 = Wizard('Marline', 50)
archer1 = Archer('Robin', 400)

#wizard1.attack()
archer1.attack()
#archer1.sign_in()



#def player_attack(char):
   # char.attack()
    
#player_attack(wizard1)
#player_attack(archer1)




#for char in [wizard1, archer1]:
    #char.attack()















        

