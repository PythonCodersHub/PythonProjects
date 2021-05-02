class Alfa:
    def delta(self):
        print("Parent 1 method")
class Beta:
    def delta(self):
        print("Parent 2 method")
class Charlie(Alfa, Beta):
    def echo(self):
     print("child method")  
Hotel =Charlie()
Hotel.echo()
Hotel.delta()
Hotel.delta()           
               