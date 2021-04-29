# Accessing Instance Variable within a class

class Light:
    def __init__(self,name,distance,colour):
        # To inherit the address of class
        # print(self)
        self.established = 1975
        self.name = name
        self.distance = distance
        self.colour=colour
    def Name(self):
        print(f"The light mentioned is {self.name}")

light1 = Light('Torch',15,'Red')

# print(light1.distance)
# Defining Explicitly

light1.name='Flare'
#print(light1)


# print(light1.name,light1.distance)



# Static Variable : Variable that doesn't change from objects
# It is recommended to access it using Class variable than that of the object variable
# Constant for every objects

class Luggage:
    carrier = 'Bag'
    def __init__(self,name,weight):
        self.name = name
        self.weight=weight

# carry = Luggage('Duffel',3)
# Recommended method is to access through Class method
# print(Luggage.carrier)

# print(carry.carrier)

class Dog:
    LEGS = 4
    EARS =2
    def __init__(self,name,place,age):
        self.name=name
        self.place=place
        self.age=age
        print(self.EARS)
    def sound(self,name):
        self.name=name
        return f"{self.name} barks"

#dog1 = Dog('Alsetian','Germany',12)



#print(dog1.LEGS)

# Declaring Static Variable in Constructor

class Mobile:
    def __init__(self,Name,Year):
        self.Name = Name
        self.Year = Year
        Mobile.battery = 'Li-ion '
        print(Mobile.battery)
        print('Accessing from self')
        print(self.battery)
        print(self.Name)
        

# mobile1 = Mobile("Nokia",2012)

# Declaring Static Variable inside class method

class Dummy:
    @classmethod
    # cls has to be passed for classmethod like self
    def Pacifier(cls):
        # Defining using class name
        Dummy.values = 745
        print(baby.values)
        print(Dummy.__dict__)

# baby = Dummy()
# #baby.Pacifier

# print(baby)


# Defining value in Static Method using cls name

class Stag:
    @classmethod
    def Stop(cls):
        Stag.age = 5
        cls.halt=30
        print(cls.age)
        print(Stag.halt)

# tag =Stag()

# tag.Stop()


class Hyderabad:
    @staticmethod
    def captain():
        Hyderabad.name = 'Warner'
        print(Hyderabad.name)
Hyderabad.captain()