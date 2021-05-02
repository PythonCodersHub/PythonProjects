# parentclass
class Alfa:
    def a(self):

        print("The a1 method is implemented")
# parentclass included into childclass
class Beta(Alfa):

    def b(self):

        print("the b1 method is implemented") 
# string the child class in the variable defined
c = Beta()

c.a()

c.b()             

class car:
    def m(self):

        print("the car is ferrari ")
class model(car):
    def mdl(self):

        print("tge car model is sports")

sports = model()

sports.m()

sports.mdl()


class Bike:
    def name(self):

        print("the bike name is FZ-90")

class alfa(Bike):
    def model(self):

        print("the model is 560")

c = alfa()

c.name()

c.model() 

class jets:
    def commercial(self):
        print("The commercial jets are")
class supersonic(jets): 
    def defence(self):
        print("the defence jets are")
c = supersonic()
c.defence()
c.commercial()                           