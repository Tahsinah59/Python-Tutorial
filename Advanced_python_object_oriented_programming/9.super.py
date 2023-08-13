"""
Created on Tue Aug  1 18:22:41 2023
@author: Tahsinah Banu
"""

# Super


class user():
    
    def __init__(self, email):
        self.email = email
    
    def sign_in(self):
        print('Logged in')
        
    def attack(self):
        print("do nothing")
        
class Wizard(user):
    def __init__(self, name, power, email):
        super().__init__(email)
        #user.__init__(self, email)
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
        
        
wizard1 = Wizard('Marline', 50, 'marlin@gmail.com')
archer1 = Archer('Robin', 400)

wizard1.attack()
archer1.attack()
archer1.sign_in()
print(wizard1.email)

#print(isinstance(wizard1,user))
#print(isinstance(wizard1,object))
#print(isinstance(user,object))
















        

