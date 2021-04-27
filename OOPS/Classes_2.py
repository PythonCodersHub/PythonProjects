# In the Constructor method __init__ should be used

class Carpet:
    def __init__(self,place,colour,life):
        self.place = place
        self.colour = colour
        self.life = life
        print(f'I want {self.place}')
    def Coating(self,desired):
        self.desired = desired
        print(self.place)

# my_carpet = Carpet('Kurnool','Dark Blue',14)

# print(my_carpet)

# my_carpet.Coating('Blue')

# Instance Variables

# For every object , we are initially passing variables they are 
# known as Instance Variables

class Seeds:
    # Constructor Method
    def __init__(self,name,activity):
        self.name = name
        self.activity=activity
    # Instance Method
    def Place(self,place):
        self.place = place
        return f'These are present near {place}'

first = Seeds('Popping Pod','Pop')
print(f'Address of first is {id(first)}')
second = Seeds('Date','Growth')
print(f'Address of Second is {id(second)}')

third = Seeds('Popping Pod','Pop')
print(f'Address of third is {id(third)}')


print(first.Place('Ponds'))
