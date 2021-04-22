""" Procedure Oriented: Programs which flow from top to bottom, which are 
compiled are known as function oriented programs


Object Oriented: Flows from bottom to top,an instance has to be created
and called, this procedure is known as object oriented.



class Student:
	name = 'Jango'
	age = 23
	def __init__(self,id,no):
		self.id = id
		self.no = no
 """


# class Bird:
#     name = 'Eagle'
#     country = 'Cosmo'

#     def __init__(self,colour,span):
#         self.colour=colour
#         self.span=span

#     def details(self):
#         print(f'Bird is {self.name}')
#         print(f'The bird is {self.colour} colour')
#         print(f"Bird's wing span is {self.span} metres.")

# # Creating an instance from the function

# first_bird = Bird('Brown',2)

# first_bird.details()

# class Vehicle:
#     # Attributes
#     Name = 'Car'
#     Mileage = 15
#     Speed = 120

#     # Methods
#     def nitro(self):
#         return self.Speed +50
    
#     def mil(self):
#         return self.Mileage / 20 

# # Creating an instance of the Vehicle class
# # Object 

# polo = Vehicle()
# print(polo.Name)
# print(polo.nitro())


# class Vehicle:
#     # Attributes
#     Name = 'Car'
#     Mileage = 15
#     Speed = 120
#     # Constructor Method
#     def __init__(self,Name,Mileage,Speed):
#         self.Name = Name
#         self.Mileage = Mileage
#         self.Speed = Speed
#     # Methods
#     def nitro(self):
#         return self.Speed +50
    
#     def mil(self):
#         return self.Mileage / 20 

# # Creating an instance of the Vehicle class
# # Object 

# polo = Vehicle('Polo',10,2012)
# print(polo.Name)
# #print(polo.nitro())


class Bird:

    def __init__(self,name,colour,span):
        self.name = name
        self.colour = colour
        self.span = span

    def display(self,country):
        
        return f'{self.name} is from {country}'

    def diet(self,prey):
        return f'{self.name} from {country}  eats {prey}'
auto = Bird('Eagle','Brown',1)

print(auto.display('India'))

print(auto.diet('Mouse'))


class Paint:
    def __init__(self,name):
        self.name = name
        print(self)
        print(self.name)
        print('Constructor is defined')

p = Paint('Red')
print('Done !')
p.__init__('Violet')

print('Done')