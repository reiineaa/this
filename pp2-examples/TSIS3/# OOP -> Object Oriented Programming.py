# OOP -> Object Oriented Programming
# Inheritance 
# Encapsulation
# Polymorphism
# Abstraction


class Bears():
    # Bears -> fur, claws, fangs, weight, height
    def __init__(self, fur_param, claws_param, fangs_param, weight_param, height_param): # constructor
        # __init__ -> fur_param, claws_param, fangs_param, weight_param, height_param
        self.fur = fur_param
        self.claws = claws_param
        self.fangs = fangs_param
        self.weight = weight_param
        self.height = height_param
    
    def run(self):
        print("The Bear is running")
        
    def hunt(self):
        print("The Bear is hunting")
        
    def swim(self):
        print("The Bear is swimming")
        
class Panda(Bears):
    bear_species = "Panda"
    def __init__(self, fur, claws, fangs,
                 weight, height, eat_bamboo):
        super().__init__(fur, claws, fangs, weight, height)
        self.eat_bamboo = eat_bamboo
        
    def run(self):
        print(f"The {self.bear_species} is running")
        
    def hunt(self):
        print(f"The {self.bear_species} is hunting")
        
    def swim(self):
        print(f"The {self.bear_species} is swimming")
        
    def panda_info(self):
        print(self.fur, self.claws, self.fangs, self.weight, self.height, self.eat_bamboo)
        
class NewPanda(Panda):
    bear_species = "NewPanda"
    def __init__(self, fur, claws, fangs,
                 weight, height, eat_bamboo, pocket):
        super().__init__(fur, claws, fangs, weight, height, eat_bamboo)
        self.pocket = pocket
        
    def run(self):
        print(f"The {self.bear_species} is running")
        
    def hunt(self):
        print(f"The {self.bear_species} is hunting")
        
    def swim(self):
        print(f"The {self.bear_species} is swimming")
        
    def panda_info(self):
        print(self.fur, self.claws, self.fangs, self.weight, self.height, 
              self.eat_bamboo, self.pocket)
        
# email -> my_email
# password -> my_password
# user = User(my_email)
        
po = Bears("Black-White", True, True, "300 kg", "2.5 m")
misha = Bears("Brown", True, True, "1 tonn", "5 m")
# print(po.fur, po.claws, po.fangs, po.weight, po.height)
# po.run()
# po.hunt()
# po.swim()
# print(misha.fur, misha.claws, misha.fangs, misha.weight, misha.height)
# misha.run()
# misha.hunt()
# misha.swim()

panda = Panda("Black-White", True, True, "250 kg", "2.2 m", "It has eaten a bamboo")
panda.panda_info()
panda.run()
panda.hunt()
panda.swim()

newPanda = NewPanda("Black-White", True, True, "250 kg", "2.2 m", "It has eaten a bamboo", "1 baby")
newPanda.panda_info()
newPanda.run()
newPanda.hunt()
newPanda.swim()