# defining parent class
class Alfa:
    def __init__(self):
        print("Class Alfa Constructor")
#defining child class 
class Beta(Alfa):
    def charlie(self):
        print("Child class of B : charlie method from B")
b = Beta()      

# child class and parent class have both constructors

class Beta:
    def  __init__(self):
        print("parent class Beta constructor")
# defining the child class
class Charlie(Beta):
    def  __init__(self):
        print("child class charlie constructor")
c = Charlie()        