"""
Created on Tue Aug  1 18:22:41 2023
@author: Tahsinah Banu
"""

# Super


class user():
    
    def __init__(self, email):
        self.email = email
        print('init complete')
    
    def sign_in(self):
        print('Logged in')
        
    def attack(self):
        print("do nothing")
        
class Wizard(user):
    def __init__(self, name, power):
        #super().__init__(email)
        #user.__init__(self, email)
        self.name = name
        self.power = power
        
    def W_attack(self):
        print(f'attacking with power with {self.power}')
        
class Archer(user):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
        
    def check_attack(self):
        
        print(f'attacking with arrows: arrows left-{self.num_arrows}')
        
        
class Hybrid(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, num_arrows)
        
        

hb1 = Hybrid('Sharlin', 50 , 500)
print(hb1.W_attack())
















        


