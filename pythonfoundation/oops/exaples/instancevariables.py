# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id   = id
#     def display(self):
#         print("The emp id is :", self.id)
#         print("The emp id is :", self.name)
# c1 = Employee('Nike', 2)
# c1.display()
# c2 = Employee('reebok', 3)
# c2.display()            


class Student:
    def __init__(self, name, id):
        self.name = name
        self.id   = id
a1 = Student('alda', 32)
a2 = Student('beta', 24)
print("Student1 info :")
print("The student1 is :", a1.name)
print("the student1 id is :", a1.id)
print("student2 info :")
print("the student2 is", a2.name)
print("the student2 id is", a2.id)    

#Declaring the instance variables inside a constructor
class Employee:
    def ___init___(self):
        self.ename = 'name'
        self.eid   = 336
        self.esal  = 250
a = Employee()
print("Employee name is :", a.ename)
print("Employee id is ", a.eid)
print("Employee salary is", a.esal)    
print(a.___dict___)
    
         