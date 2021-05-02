class Student:
    def a1(self):
        self.a = 56
        self.b = 3600
        self.c = 2500
        print(self.a)
        print(self.b)
        print(self.c)
d = Student()
d.a1()
print(d.__dict__)        

class Employee:
    def b1(self):
        self.a1 ='a'
        self.b1 = 'b'
        self.c1 = 'c'
        print(self.a1)
        print(self.b1)
        print(self.c1)
c = Employee()
c.b1()
print(c.__dict__)  

# Declaring instance variables using object name

class Game:
    def a1(self):
        print("the game constructor")
g = Game()
g.a1()
g.a = 20
g.b = 30
g.c = 40
print(g.a) 
print(g.b) 
print(g.c)
print(g.__dict__)         

# Accessing instance variable:
# -	By using self variable
class Student:
    def __init__(self):
        self.a = 10
        self.b = 10
    def display(self):
        print(self.a) 
        print(self.b)
s = Student()
s.display()        

# By object name:

class Student:
    def __init__(self):
        self.a = 30
        self.b = 40
    def display(self):
        print(self.a)
        print(self.b)
s= Student()
print(s.a)
print(s.b)        
           
    