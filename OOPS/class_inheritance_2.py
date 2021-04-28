# Method Resolution Order

class GreatGrandFather:
    def Root(self):
        print('My Child will inherit 50 acres')

class GrandFather:
    def Root(self):
        print('My Child will inherit 70 acres')

class Father:
    def Root(self):
        print('My Child will inherit 40 acres')

class Child(Father,GrandFather,GreatGrandFather):
    def Roots(self):
        print('My Child will inherit 30 acres')

take = Child()

#take.Root()

class A:
    def __init__(self,name):
        self.name = name
    
    def printing(self):
        print(self.name)
    
class B(A):
    def __init__(self,age):
        self.age = age
        super().__init__("Jango")
    
    def printings(self):
        print(self.age)
       

call = B(12)

# call.printings()

class A():
    def m1(self):
        print("m1 from class A")

class B:
    def m1(self):
        print("m1 from class B")

class C(A):
    def m1(self):
        print("m1 from class C")
class D(B,C):
    def m3(self):
        print("m1 from class D")
    
class E(D,A):
    def m2(self):
        print('m1 from class E')


# A.mro()

# e = E()
# e.m1()


class A:
   def m1(self):
       print("m1 from A")
class B:
   def m1(self):
       print("m1 from B")
class C:
   def m1(self):
       print("m1 from C")
class X(B,A):
   def m1(self):
       print("m1 from C")
class Y(B,C):
   def m1(self):
       print("m1 from A")
class P(X, Y, C):
   def m1(self):
       print("m1 from P")
# print(A.mro())#AO
# print(X.mro())#XABO
# print(Y.mro())#YBCO
# print(P.mro())#PXAYBCO

class A:
    class_variable= 25
    def m1(self,name):
        self.name=name
        print('Super Class A , method m1 ',self.name)
    
class B(A):
    new_variable = 15
    def m1(self):        
        print('Child Class B, method m1')
        super().m1('Anil')
        print(self.new_variable)
        print('Super Class Variable',super().class_variable)

calls = B()

calls.m1()