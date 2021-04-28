class Furniture:
    def __init__(self,name):
        self.name=name
        print('THis is Room imput',self.name)

class Room(Furniture):
    def __init__(self,age):
        self.age=age
        return None

    def Above(self,material):
        self.material=material
        print(self.age)
        super().__init__('Top Class')
        return f'Available furniture is of {self.material}'
    

# Search = Room(5).Above('Wood')

class A:
   def m1(self):
       print("m1 from A")
class B(A):
   def m1(self):
       print("m1 from B")
class C(A):
   def m1(self):
       print("m1 from C")
class D(B, C):
   def m3(self):
       print("m3 from D")

# d=D()
# d.m1()
# print(D.mro())

class First:
    def Value(self):
        print('Value from First Class')
class Second:
    def Value(self):
        print('Value from Second Class')
class Third(First):
    def Value(self):
        print('Value from Third Class')
class Four(Third):
    def Value(self):
        print('Value from Four Class')
class Five(Third,Second):
    def Value(self):
        print('Value from Four Class')

print(Five.mro()) 


class A:
   def m2(self):
       print("m1 from A")
class B(A):
   def m1(self):
       print("m1 from B")
class C(A):
   def m2(self):
       print("m1 from C")
class D(B, C):
   def m3(self):
       print("m3 from D")

# d=D()
# d.m2() # m1 from  C as B,C are the parent classes of D, while A is the parent class of B,C
# print(D.mro()) 


class A:
   def m1(self):
       print("m1 from A")
class B:
   def m1(self):
       print("m1 from B")
class C:
   def m1(self):
       print("m1 from C")
class X(A,B):
   def m1(self):
       print("m1 from C")
class Y(C,B):
   def m1(self):
       print("m1 from A")
class P(X, Y):
   def m1(self):
       print("m1 from P")
# print(A.mro())
#print(X.mro())
#print(Y.mro())
# print(P.mro())


class A:
    z=5
    def m1(self):
        print("m1 from A")
class B:
    x=12
    def m1(self):
       print("m1 from B")
class C:
    z=23
    def m1(self):
       print("m1 from C")
class X(C,A):
    x=34
    def m1(self):
       print("m1 from C")
class Y(A,B):
    y=345
    def m1(self):
       print("m1 from A")
class P(Y,X):
    x=234
    def m1(self):
        print("m1 from P")
        print(super().y)

# print(P.mro())
 

class A: 
    def m1(self):
        print("m1 from A")
class B:
    def m1(self):
        print("m1 from B")
class C:
    def m1(self):
        print("m1 from C")
class X(A,B):
    def m1(self):
        print("m1 from C")
class Y(B,C):
    def m1(self):
        print("m1 from A")
class P(Y,X):
    def m1(self):
        print("m1 from P")
# print(A.mro())#AO
# print(X.mro())#XABO
# print(Y.mro())#YBCO
# print(P.mro())#P


#  Accessing Different Values
class A:
    value =1
    def Namer(self):
        print(self.value)
        print('Class A')
class B:
    value = 2
    def Namer(self):
        print(self.value)
        print('Class B')
class C:
    value = 3
    def Namer(self):
        print(self.value)
        print('Class C')
class X(A,B):
    # value = 4u
    def Named(self):
        print('Class X')
class Y(B,C):
    # value = 5
    def Named(self):
        print(self.value)
        print('Class Y')
class P(X,Y):
    # def Names(self):
    #     print(self.value)
    #     # print('Class P')
    #     super().value

new = P()
new.Namer()