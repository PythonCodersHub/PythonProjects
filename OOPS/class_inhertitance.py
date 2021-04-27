class Day:
    def Morning(self):
        print('Good Morning')
    
    def Evening(self):
        print('Good Evening')

class Greet(Day):
    def Greet(self):
        print('Greetings !')

hello = Greet()
# print(dir(Greet))
# hello.Morning()


class Car:
    Vehicle_Type = 'Car'
    def __init__(self,Name,Colour):
        self.Name=Name
        self.Colour=Colour
    
    def Parking(self):
        print(f"I parked my {self.Colour} coloured {self.Name}")

class Place(Car):    
    def Find(self,Area,Name):
        self.Area=Area
        self.Name=Name
        print(f"He parked his  {self.Colour} {self.Name} {self.Vehicle_Type} at {self.Area}")

# find_first_car = Place('Swift','White')
# find_first_car.Find('Top','Polo')


#  Multi Level Inheritance
class FirstGeneration:
    def GrandFather(self):
        print('My child inherits 75 acres of land from me')

class SecondGeneration(FirstGeneration):
    def Father(self):
        print('My child inherits 50 factories from me')

class ThirdGeneration(SecondGeneration):
    def GrandSon(self):
        print('My Child inherits 25 buildings from me')

great_grandson = ThirdGeneration()

first = FirstGeneration()

# Multiple Inheritance


class Paternal:
    def Will(self):
        print('My child Will inherit 75 acres of land from me')

class Maternal:
    def Wills(self):
        print('My child Will inherit 575 acres of land from me')

class Child(Paternal,Maternal):
    def All(self):
        print('I will inherit everything from maternal and paternal')

take = Child()

take.Wills()