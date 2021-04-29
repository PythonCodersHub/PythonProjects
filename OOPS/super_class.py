# class A:
#     def m1(self,name):
#         self.name=name
#         print(self.name)
#         print('Class A')

# class B(A):
#     def m1(self):
#         print('Class B')

# class C(B):
#     def m1(self):
#         C.m1(self)
#         print('Class C')

# class D(C):
#     def m1(self):
#         print('Class D')
#         # Calling parent class from the child class
#         A.m1(self,'Gowrav')
#         B.m1(self)

# sup = D()

# sup.m1()


class A:
    def m1(self):
        print('Class A')
    
    def m2(self):
        print('CLass A 2')

class B(A):
    def m3(self):
        print('Class B')

class C(B):
    def m1(self):
        print('Class C')

class D(C):
    def m1(self):
        print('Class D')
        # Calling parent class from the child class
        super(D,self).m1()
        #super(B,self).m2()
        super(D,self).m2()  
sup = D()

# sup.m1()
# sup.m3()

class A:
    name='Python'
    def __init__(self,name,age):
        self.a=20
        self.age=age
        self.name=name
    
    # def display()


class B(A):
    def m1(self):
        #print(super().name)
        # Variables in the parent class can only be access using self
        print(self.age,self.name)

instance = B('Python',23)
instance.m1()

