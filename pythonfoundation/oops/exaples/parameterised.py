# defining class
class Employee:
# defining the constructor 
    def __init__(self, id):
        self.id = id
        print("The employee id is", self.id)
#storing the obj 
a1 = Employee(1)
a2 = Employee(2)   

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id   = id
    def display(self):
        print("The employee name is", self.name)
        print("The emp id is", self.id)
a1 = Employee(22, 'chary')
a1.display()
a2 = Employee(44, 'battu')
a2.display()                 