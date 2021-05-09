#--------------------------------------------------------Polymorphism---------------------------------------------------------
class Infant:
    def gait(self):
        print('Toddle')

class Child:
    def gait(self):
        print('Dash')
    
    def play(self):
        print('Flute')

class Teen:
    def gait(self):
        print('Tip-Toe')
    
    def hair(self):
        print('Long')

class Adult:
    def gait(self):
        print('Strut')

def Style(person):
    person.gait()
    person.play()

kid = Infant()

# Style(kid) # As there is no method named play in the class

# Style(Child()) # No error as the class has the methods defined the Style UDF

# ----------------------------------------------------Operator Overloading-----------------------------------------------------
# Addition Operator : This can be used for addition of numbers and concatenating the strings

number1 = 1
number2 = 2

# print(number1+ number2)

string1 = '1'
string2 = '2'

# print(string1+string2)


# Multiplication Operator : This can be used for addition of numbers and concatenating the strings

number1 = 3

# print(number1*3) 

string1 = '3'

# print(string1*3)

# ------------------------------------------------------Method Overloading---------------------------------------------------------

class Flight:
    def call(self):
        print(' First Call')
    
    def call(self):
        print('Second Call')
    
    def call(self):
        print('Third Call')
    
    def call(self):
        print('Final Call')

flee = Flight()

# flee.call() # Fourth Call will be printed as the python method overloading allows to take the last defined method

class Pen:
    def board(self):
        print('Pen is empty')
    
    def board(self, stock,count):
        self.stock = stock
        self.count=count
        print(f"There are {self.count} {self.stock}'s in the pen")
    

    def board(self,feed):
        weight= 6
        self.feed=feed
        print(f"There is {weight} tons of {self.feed}  in the pen")
    
pen1 = Pen()

# pen1.board() # This results in a error as an argument needed to be passed to this

# pen1.board('Cow',150) # This results in same error as above as only argument to be passed to the class

# pen1.board('Straw') 

# Varible Length Argument

class VaribleLengthArgument:
        def numbers(self,*row):
            res =1
            for i in row:
                res*=i
            print(res)
# VaribleLengthArgument().numbers(4,5,6)

#----------------------------------------Constructor Overloading-------------------------------------

class ConstructorOveLoading:
    def __init__(self):
        print('No Argument')
    
    def __init__(self,one):
        print('One Argument')
    
    def __init__(self,one,two):
        print('Two Arguments')

    def __init__(self,one,two,three):
        print('Three Arguments')

# ConstructorOveLoading(1,2,3)  # Takes three arguments as the last constructor was initiated with 3 attributes

class Infinite:
    def __init__(self,*indefinite):
        print(f'Passed Values are {indefinite}')

# Infinite(1,2,3,4,5,6,7,8,9,10)

#---------------------------------------------------------------Over Riding----------------------------------------------

class India:
    def Area(self):
        print('3.28 Square Million kms')
    
    def Language(self):
        print('Hindi')

class Andhra(India):
    def Location(self):
        print("South")
    
    def Language(self):
        print("Telugu")

telugu = Andhra()

# telugu.Language()