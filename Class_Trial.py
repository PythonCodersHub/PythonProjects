class Clothes:
    category = 'Lifestyle'
    # Constructor Method
    def __init__(self,shirt,trouser):
        self.shirt=shirt
        self.trouser=trouser
    # Instance Method  
    def Colour(self,shirt_colour,trouser_colour):
        self.shirt_colour=shirt_colour
        self.trouser_colour=trouser_colour
        print(f'The person desires {self.shirt_colour} coloured {self.shirt} with {self.trouser_colour} {self.trouser}')
      

# first_person = Clothes('Polo','Track')

# second_person = Clothes('Striped','Cotton')

# first_person.Colour('white','purple')


class Go:
    way = 'Fly'
    threshold = 10
    luxury = "Charter"
    economy = "Boeing"
    def __init__(self,aircraft,travellers,time):
        self.aircraft=aircraft
        self.time=time
        self.travellers=travellers

    def suggestion(self):
        if self.travellers>self.threshold or self.time>self.threshold:
            # Accessing the global variable using instance of class
            print(f'Fly in {trip.economy}')
        else:
            print(f"Fly {trip.luxury}")


# trip = Go("Boeing",2,5)

# trip.suggestion()

#  Declaring instance variables using objects

class Kafka:
    def Wiki(self):
        print('No details were known by this name')

franz = Kafka()
franz.occupation = 'Clerk'
franz.lingo = 'German'
franz.style = 'Bohemian'

# print(franz.__dict__)

# print(dir(franz)) #  To check the instances present in the  object

# george  =Kafka()

# print(dir(george)) # This class wouldn't have any instances, as instance variables are delcared in the franz object

# Accessing the instance variables using object

class Pick:
    def __init__(self):
        self.first='Gold'
        self.second='Diamond'
        self.third='Coal'

dip = Pick()

# print(dip.first)
# print(dip.second)
# print(dip.third)

# Using Static Variables

class Shops:
    # Here all the available items are fruits, we created a variable that says the items as fruits
    section='Fruits'
    Cost = 25
    def __init__(self,name,quantity):
        self.name=name
        self.quantity=quantity
    
    def Invoice(self):
        #  Accessing the static variable using Class and object name
        print(f" In the {Shops.section} section your bill is {self.quantity * Shops.Cost} rs for {self.quantity} {self.name}")

# Initialising the object name as mango 
mango = Shops('Mango',50)

# Accessing the Static Variables using object
#print(mango.section)
# Accessing the cost variable using Class 
# print(Shops.Cost)

# print(mango.__dict__)

# mango.Invoice()

#  Second instance
# apple = Shops('Apple',30)
# apple.Invoice()

# Declaring static variable inside class and outside of the method
class Hole:
    tool="Crowbar"
    #@staticmethod
    def dig(self):
        print(f'You need a {Hole.tool} to dig')
# make = Hole()
# make.dig()

# Variables that are declared with in the class can be accessed using class,while declared in constructor or instance methods
# can only be accessed through self method
# print(Hole.tool)
# To check the attributes present in the object
# print(dir(make))

#Declaring static variable inside constructor

class Fire:
    def __init__(self,name):
        #  Defining a static variable in the constructor
        self.speed=1200
        self.name=name
        self.colour=colour
        print(f'Bullet from {self.name} travels {Fire.speed} kmph')

# gun = Fire('Rifle')
# print(Fire.speed)
# print(dir(gun))
# gun2 = Fire('AK47')

class Bag:
    new='SOmething'
    def cloth(self,cloth):
        self.duration='Long'
        self.cloth=cloth
        print(f'{self.cloth} have {Bag.duration} duration')

# cot = Bag()
# cot.cloth('Cotton')
# Static Variables defined in the Constructor and Instance methods cannot be accessed by calling from class

# print(Bag.duration)

""" 
A class method receives the class as implicit first argument, just like an instance method receives the instance. 
To declare a class method, use this idiom:
class C:
    @classmethod
    def f(cls, arg1, arg2, ...): ...
The @classmethod form is a function decorator 
The instance is ignored except for its class. If a class method is called for a derived class, the derived class object is 
passed as the implied first argument.
"""

class Cook:
    @classmethod
    def Pop(cls): # THis method takes cls as the first arugment rather than self 
        Cook.time=15
        print(cls.time)
        cls.whistle=10
        print(Cook.whistle)
# wheez = Cook()
# wheez.Pop()

# Static Method
class Hyderabad:
    @staticmethod
    def captain():
        # With in a class the variables can be accessed only through Class name
        Hyderabad.name = 'Warner'
        print(Hyderabad.name)
Hyderabad.captain()
