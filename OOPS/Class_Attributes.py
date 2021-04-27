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


class Calculator:
    def Addition(self,number1,*number2):
        new_list = list(number2)
        new_list.append(number1)
        return sum(new_list)
    
    def Multiplication(self,number1,*number2):
        new_list = list(number2)
        new_list.append(number1)
        prod = 1
        for i in new_list:
            prod*=i
        return prod


calci = Calculator()
print(calci.Addition(1,2,3,6,4,8).__dict__)

#print(calci.Addition.__dict__)