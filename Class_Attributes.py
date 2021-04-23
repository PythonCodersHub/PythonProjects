class Fly:
    def __init__(self,means,destination,speed):
        self.means=means
        self.destination=destination
        self.speed=speed
    
    def eta(self):
        milometer=1500
        return f"You can reach {self.destination} by {round(milometer/self.speed,2)} HOURS"

sprint= Fly('Carpet','Kanyakumari',120)

# print(sprint.eta())

# Deleting an attribute from an instance
del sprint.destination

# print(sprint.eta())


