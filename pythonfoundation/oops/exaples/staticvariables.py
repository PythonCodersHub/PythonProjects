# STATIC VARIABLES
# Accessing static variables outside of class
# Accessing static variables with class name
class Student:
    college_name = 'IIt b'
    def __init__(self, name, id):
        self.name = name
        self.id = id
s1 = Student('Alfa', 33)
s2 = Student('Beta', 45)

print("the student name is", s1.name)
print("The student id is", s1.id)
print("The college name is ", Student.college_name)

print("\n")
print("The student name is", s2.name)
print("The student id is", s2.id)
print("The college name is ", Student.college_name)        

# Accessing static variables with object name
class Student:
    college_name = 'NIT'
    def __init__(self, name, id):
        self.name = name
        self.id   = id
a1 = Student('Bat', 336)
a2 = Student('PAds', 636)

print("Student1 info")
print("the student name is", a1.name)
print("the student  id is", a1.id)
print("The college name is ", Student.college_name)        

print("\n")
print("the student name us ", a2.name)
print("the student id is ", a2.id)        
print("The college name is ", Student.college_name)  



#Declaring static variable inside class and outside of the method

class Kaali:
    b = 20
    def a(self):  
        print("This is a demo methos")
print(Kaali.__dict__)         

# Declaring static variable inside constructor
class Demo:
    # construtctor
    def __init__(self):
        Demo.b = 20
c = Demo()
print(Demo.__dict__)        

# Declaring static variable inside instance method
class Car:
    def m1(self):
        Car.b = 20
obj = Car()
obj.m1()


# Declaring static variable inside class method
class Cars:
    @classmethod
    def m1(self):
        Cars.b = 50
obj =Cars()
obj.m1()
print(Cars.__dict__)

# static variable inside class method by using cls         

class Books:
    @classmethod
    def c1(cls):
        cls.b = 20
obj = Books()
obj.c1()
print(Books.__dict__)   

# static variable inside static method by using class name     
# class Book:
#     @classmethod
#     def m3():
#         Book.a = 20
# Book.m3()
# print(Book.__dict__)   

# Accessing a static variable within the class
# Inside Constructor
class Dell:
    a =10
    def __init__(self):
        print(self.a)
        print(Demo.a)
d = Demo()        

# Inside instance method

class Dell:
    a = 20
    def m1(self):
        print(self.a)
        print(Dell.a)
obj = Dell()
obj.m1()       

# Inside classmethod: 
class Dell:
    b = 20
    @classmethod
    def m1(cls):
        print(cls.b)
obj=Dell()
obj.m1()         
        

        