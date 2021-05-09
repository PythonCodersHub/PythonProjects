# class Predator:
#     @abstractmethod
#     def detail(self,name,place):
#         self.name = name
#         self.place = place
#     def info(self):
#         print(f'Enter is known as {self.name} found in {self.place}')


# class Prey(Predator):
#     def __init__(self,name,place,quarry):
#         super().__init__(name,place)
#         self.quarry=quarry

#     def catch(self):
#         print(f'{self.name} eats {self.quarry}')
    

# kill = Prey('Orca','Antarctica','Weddell')

# # kill.catch()

# Abstract method are only to be implemented in the child class
from abc import ABC,abstractmethod

class Wire(ABC):
    def fibre(self,name):
        print('Fibre Cable',name)
    
    @staticmethod
    @abstractmethod
    def look(thickness):
        print('Thick',thickness)
    
# Any class with the presence of abstract method can't be used to instantiate an object
class Optical(Wire):
    @staticmethod
    def look():
        print('Thin')
    
    @staticmethod
    def speed():
        print('30')

# new = Wire.fibre('self','Som')

wire = Optical()

wire.look()

# clear = Wire()