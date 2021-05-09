class Clothing:
    def __init__(self,name,cloth):
        self.name=name
        self.cloth=cloth
        print(self.cloth,self.name) # To print the values given

class Men(Clothing):
    def __init__(self,cost,duration):
        self.cost=cost
        self.duration=duration
    def display(self):
        super().__init__('Jacket','Leather') # Initialising the values of super class from child class
        print(self.cost,self.duration)
        
    
# Men(1200,2).display()

# Parent Class and Child Class with same variables

class Stone:
    strength = 50
    pass

class Clod(Stone):
    strength = 20
    def Hit(self):
        print(f'Hit the git with {super().strength} gms stone') # Using super retrieves the globally defined variable
        print(f'Hit the git with {self.strength} gms Clod')  
        """ Using self retrieves the locally available variable if the variable name of global and local variable is initiated with
        same name """
         
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
      
# e=E()
# e.m1()

# Accessing Class Variables using super

class Road:
    roll='Wheels'
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed
    def Ride(self):
        colour = 'Blue'
        print('Wheels are to roll')

class Lights(Road):
    def vision(self):
        super().Ride() # Calling instance method using super
        print(super().roll) # super() can be used to access the static variables that are defined in the class
        print('Lights are used for vision at night !')
       
# bent = Lights('Bentley',350)jl
    
    def Available(self):
        print(self.prime,self.mix)

class Evening(Food):
    def Display(self):
        print(super().eat) # Accessing the static variable using super 
        print(self.mix,self.prime) # Accessing the variables in the method using self

# evening = Evening('Dosa','Chutney')

# evening.Display()

# Accessing the Static Method in the parent class

class King:
    name,will='Charles',2300
    def __init__(self):
        print('Welcome to Buckingham Palace')
    def Portrait(self):
        print(f'King {self.name} has written {self.will} to his heir')

    @classmethod
    def Heirloom(cls):
        cls.item="Sceptor"
        print(f'The heirloom is {cls.item}')

    @staticmethod
    def Palace():
        print('New Home is Buckingham Palace')

    def Heirs(self,number):
        self.number=number
        print(f'There are more than {self.number} heirs in the line of succession')


class Prince(King):
    def __init__(self,monicker,age):
        self.age=age
        self.monicker=monicker
    def Succession(self):
        print(f'Prince {self.monicker} will be crowned as King at {self.age} years old')
    def Telly(self):
        super().__init__() # Accessing the Constructor class of parent class using child class
        super().Heirs(12) #Accessing the instance Method Using Super
        super().Portrait() # Accessing the instance method
        super().Heirloom() # Accessing the Class method
        super().Palace() # Accessing the Static methid
        print(self.item) # Accessing the variable of class method    
        
phil = Prince('William',34)
# phil.Telly()

# Willing = Parent('George',2300)

# Willing.Heirloom('Sceptor')

# Willing.Portrait()

class SolarSystem:
    def place(self):
        print('Earth')

class Continent(SolarSystem):
    def place(self):
        print('Asia')
    
class Country(Continent):
    def place(self):
        print('India')
    
class Part(Country):
    def place(self):
        print('South')
    
class State(Country):
    @classmethod
    def place(cls):
        print('Telangana')

class City(State):
    def place(self):
        print('Hyderabad')

class GlobalPosition(City):
    def place(self):
        City.place(self) # Accessing the method calling directly the class name
        super(State,self).place() # Accessing the parent class from the super method

class GlobalPosition(City):
    @classmethod
    def place(cls):
        City.place(cls)
        super(State,cls).place(cls) # Calling the INstance method of the Parent Class from the child with class method 


find_me = GlobalPosition()

# find_me.place()


class P:
   def __init__(self):
       print('Parent Constructor')
   def m1(self):
       print('Parent instance method')
   @classmethod
   def m2(cls):
       print('Parent class method')
   @staticmethod
   def m3():
       print('Parent static method')
class C(P):
   @classmethod
   def m1(cls):
        super(C, cls).__init__(cls)
        super(C, cls).m1(cls)  

C.m1()




