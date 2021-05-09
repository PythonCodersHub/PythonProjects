""" Poly means many and Morphs means forms """

class Duck:
    def sound(self):
        print('Quack..Quack')

class Dog:
    def sound(self):
        print('Bow..Bow')

class Cat:
    def sound(self):
        print('Meow..Meow')

class Tom:
    def cry(self):
        print('Purr..Purr')

def zoo(call): # Pass an object as parameter
    call.sound() # Calling the method of object passed as the parameter
    call.cry()

# duck = Duck()
# zoo(duck)

# tom = Tom()
# zoo(tom) # THis results in an error as the object doesn't have the other method 


#-----------------------------------OVERLOADING-------------------------------
#--------------------------------------OPERATION OVERLOADING----------------------

class Farm:
    def __init__(self,number):
        self.number = number
    
farm1 = Farm(100)
farm2 = Farm(200)
farm3 = Farm(300)

# print(type(farm1.number))

# print(farm1.number + farm2.number)
# print((farm1.number).__add__(farm2.number).__add__(farm3.number)) # add is a dunder function in OOPS



#------------------------------------------------------OVERLOADING THE ADDITION METHOD-------------------

class Farm:
    def __init__(self,number):
        self.number = number
    
    def __add__(self,others):
        return self.number + others.number
    
    def __mul__(self,others):
        return self.number * others.number
    
    def __init_subclass__(self,name):
        self.name = name
        print(self.name)
farm1 = Farm(100)
farm2 = Farm(200)
farm3 = Farm(300)


# print(farm1.__add__(farm2,farm3))

#----------------------------------------------------METHOD OVERLOADING--------------------------------
# If two methods have same name, then the class object will always take the last method

class MethodOverloading:
    def first(self,name):
        self.name = name
        print('First method')
    def first(self,name,number):
        self.name = name
        self.number = number
        print('Second method')

met = MethodOverloading()

met.first('Gowrav',12)

