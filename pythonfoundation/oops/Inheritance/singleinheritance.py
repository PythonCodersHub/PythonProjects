# parent class or superclass
class A:
    def Beta(self):
        print("Beta is defined function for class A")
# child class or subclass
class B(A):
    def Charlie(self):
        print("charlie is defined as the function for the subclass") 
obj = B()
obj.Beta()
obj.Charlie()      

class cars:
    def mercedes(self):
        print("name of the car is mercede")
class models(cars):
    def model(self):
        print("the model of the cars is s-360")
obj = models()
obj.mercedes()     
obj.model()
             
                 
class Bikes:
    def name(self):
        print("the name of the bike is Yamaha")
class models(Bikes):
    def model(Bikes):
        print("the model of the bike is yz360")
object = models()
object.name()
object.model()                

                