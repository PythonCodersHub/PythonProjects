# Accessing a static variable within the class

class External:
    device = "EarPhones"
    dB = 70
    @staticmethod
    def __init__(self):
        # Accessing  static variable in the constructor using self
        print(self.device,External.dB)
        # Accessing static variable in the constructor using Class Name
        print(External.device,self.dB)
    
    def Listen(self):
        print('Accessing Static Variable inside the instance method using self and Class')
        print(self.device),print(External.dB)

# sony = External()

# sony.Listen()

# For the class method, we can access the static variables using class method and cls method

class Dustman:
    collects="Rubbish"
    @classmethod  # @classmethod is not necessary , but has to be defined for understanding purpose
    def Cart(cls):
        print(cls.collects)
        print(Dustman.collects)

# dust = Dustman()

# dust.Cart()
# Accessing static variables using object method
#print(dust.collects)

# Static Method
# They can only be accessed using Class name

class Dustman:
    collects="Rubbish"
    @staticmethod  # @classmethod is not necessary , but has to be defined for understanding purpose
    def Cart():
        #print(self.collects)
        print(Dustman.collects)
        #They can also be accessed using objects
        print(dust.collects)

# dust = Dustman()

# dust.Cart()


# Local Method

class Local:
    def access(self):
        # Locally defined variables cannot be accessed anywhere
        create='Locally'
        print(create)

    def instance_access(self):
        print(create) # Results in error , as the variable is created in another method
# loc = Local()

# loc.access()
#loc.instance_access()  # This would result in error as the variable is not defined


# Instance Methods

class Name:
    def __init__(self,name):
        self.name=name
    
    def display(self):
        print(self.name)

# my_name = Name('Gowrav')

# my_name.display()


"""
Setter and inheritter Methods
 """
class Setinherit:
    def __init__(self,name):
        # This is the setter
        self.name = name
    
    def SetUp(self,id):
        self.id=id

#Setter Method
# s = Setinherit('Nani')

# # inheritter Method
# print(s.name)

#  Class Method

class Pizza:
    radius=35
    @classmethod
    def inherit_radius(cls):
        return cls.radius

#  Can be accessed using Object
# print(Pizza.radius)

# p = Pizza()
# #  Can be accessed using Object
# p.inherit_radius()




#  Static Method

class Calci:

    @staticmethod
    def sum(x,y):
        print(x+y)

    @staticmethod
    def product(x,y):
        print(x*y)

# Calci.sum(1,2)

#Calci.product(3,4)

# Accessing variables using object
casio=Calci()

casio.product(7,8)