class Vehicle:
    def __init__(self,name,company):
        self.name = name
        self.company = company
    
    def year(self):
        return self.name,self.company

inst = Vehicle("Polo","VW")

print(inst.year)

class Computer:
    def config(self):
        print("Nothing")
    
Computer.config("some")