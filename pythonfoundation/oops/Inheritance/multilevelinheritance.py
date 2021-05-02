# parentclass or superclass
class A:
    def alfa(self):
        print("Parent class is A : method is alfa")
# childclass or subclass B
class B(A):
    def beta(self):
        print("child classes B derived from A : method is beta") 
# grandchild or child class or subsubclass C
class C(B):
    def charlie(self):
        print("child classes C derived from B : method is charlie")
obj = C()
obj.alfa()
obj.beta()
obj.charlie()                       