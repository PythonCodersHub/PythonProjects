class Clothing:
    def __init__(self,name,cloth):
        self.name=name
        self.cloth=cloth
        print(self.cloth,self.name)

class Men(Clothing):
    def __init__(self,cost,duration):
        self.cost=cost
        self.duration=duration
    def display(self):
        super().__init__('Jacket','Leather')
        print(self.cost,self.duration)
        
    
# Men(1200,2).display()

# Parent Class and Child Class with same variables

class Stone:
    strength = 50
    pass

class Clod(Stone):
    strength = 20
    def Hit(self):
        print(f'Hit the git with {super().strength} gms stone')
        print(f'Hit the git with {self.strength} gms Clod')

# fly = Clod()

# fly.Hit()

# Parent class and Child class with same methods

class Chair:
    def __init__(self,name,shape,capacity):
        self.name=name
        self.shape=shape
        self.capacity=capacity
    
    def display(self):
        print(self.name)
        print(self.shape)
        print(self.capacity)

class Stacks(Chair):
    def __init__(self,name,shape,capacity,colour,movement):
            super().__init__(name,shape,capacity)
            self.colour=colour
            self.movement=movement
    
    def display(self):
        # To display the methods present in the Parent Class with the same name
        super().display()
        print(self.colour)
        print(self.movement)

lawn = Stacks('Swivel Chair','4',1,'Black','Drag')

# lawn.display()



class A:
   def m1(self):
       print('m1() method from A class')
class B(A):
   def m1(self):
       print('m1() method from B class')
class C(B):
   def m1(self):
       print('m1() method from C class')
class D(C):
   def m1(self):
       print('m1() method from D class')
class E(D):
   def m1(self):
       #A.m1(self)
       super(D, self).m1()
      
e=E()
e.m1()














