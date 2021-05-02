class Car:
    def __init__(self):
        print("Benz")
        print(self)
car = Car()        


class Bike:
    def __init__(self):
        print('Ducati')
        print(self)
bike=Bike()

# nonparameterised constructor

class Employee:
    def __init__(self):
        self.id = 2020
        print("The employee id :", self.id)
a1 = Employee()        
a2 = Employee()      
a3 = Employee()        
  
        

        