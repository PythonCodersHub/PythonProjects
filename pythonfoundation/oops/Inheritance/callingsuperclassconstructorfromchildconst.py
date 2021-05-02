class Alfa:
    def ___init___(self):
        print("The Superclass A constructor")
class Beta(Alfa):
    def ___init___(self):
        print("the child class B constructor")
        super().___init___()
        
c = Beta()        
