from abc import abstractmethod,ABC
#  Implemented Method 
""" The method which has its name but no body is present """


class Painting(ABC):
    def Colours(self,name):
        self.name=name
        print(f'The Colour of the Sketch is {self.name}') 
    
    @abstractmethod
    def Purchase(self):
        print('Magnetic Nails')

#wall = Painting() # This will results in an error as the class is a subclass of ABC
#wall = Painting().Colours('Green') # Object can be created for a non-abstract methods

# Painting().Colours('Violet') # They can also be accessed from the Class

class Winston(Painting):
    def display(self,name):
        self.name=name
        print(f'The paint is {self.name} colour ')
    
# prime = Winston() # It won't work as the child class doesn't have the abstract class implementation of the parent class,\

# it will also be considered as abstract class


#------------------------------------------------------------------------------------------------------------------------------

class Song(ABC):
    @abstractmethod
    def Singer(self):
        print('GV')
    
    def Year(self):
        print(1964)

class Tel(Song):
    def Singer(self):
        print('Ghantasala')

print(type(Song))

# phy = Tel() # An object is posssible as the child class has the abstract class method implementation as of the parent class

# phy.Singer() # Ghantasala

# phy.Year()

#------------------------------------------------------------------------------------------------------------------------------

""" Creating a abstract class with constructor class """

# Creating a abstract method without calling it as a subclass

class Painting:
    def Colours(self,name):
        self.name=name
        print(f'The Colour of the Sketch is {self.name}') 
    
    @abstractmethod
    def Purchase(self):
        print('Magnetic Nails')

class Winston(Painting):
    def Display(self,name):
        self.name=name
        print(f'The paint is {self.name} colour ')

# church = Winston()

# church.Purchase() 

#----------------------------------------------------------------------------------------------------------------------------------
# Creating a abstract class without creating abstract method 

class Carpet(ABC):
    def Origin(self,place):
        self.place=place
        print(f'Carpet is from {self.place}')
    
carpet = Carpet() # Object creation is possible 

# carpet.Origin('Solapur') 
#----------------------------------------------------------------------------------------------------------------------------------
# Interface -  Abstract Class with only abstractmethods

# Interface with two abstract methods and one sub class
class Hit(ABC):
    @abstractmethod
    def Club(self):
        print('Hit with club')
    
    @abstractmethod
    def Staff(self):
        print('Hit with staff')
    
class Clout(Hit):
    def Club(self):
        print('clout a club')

    def Staff(self):
        print('clout a staff')

# git = Clout()

# git.Club()

# One Interface and two subclasses

class Trip(ABC):
    @abstractmethod
    def Walk(self):
        print('Foot')
    
    @abstractmethod
    def Ride(self):
        print('Car')

class Country(Trip):
    def Walk(self):
        print("Ramble")
    
    def Ride(self):
        print('Bicycle')

class City(Trip):
    def Walk(self):
        print("Dash")
    
    def Ride(self):
        print('Motorcycle')


place = input("Enter the type of area you wanna visit : ")    

classname = globals()[place]

trip = classname()

trip.Walk()

trip.Ride()