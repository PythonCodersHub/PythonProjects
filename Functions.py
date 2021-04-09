'''
Positional Arguments
If we pass the actual arguments without calling the
formal arguments it is called positional arguments. It will be taken as of the index order
the actual argument is mapped to the first formal argument, so are the others was the name
positional arguments

'''
def parking_area(length,breadth):
	return f"The parking area is {length*breadth} sq.yards"


#print(parking_area(5,10)) # 5 will be mapped to length, 10 will be mapped to breadth as they are at their respective index

#print(parking_area(15,25,23)) # This would result in a error as the number of actual arguments passed are more than that of the formal arguments

'''
Keyword arguments
Positional arguments map the arguments in an order, there might be a place
where one can't remember something at that juncture or something else, so one doesn't have to stop
assigning the values. In the keyword arguments, we call the formal arguments while calling a function 
and can be assigned in any order. While assigning the arguments without calling the formal arguments is not possible
'''



def specifications(RAM,ROM):
	return f"Laptop RAM is {RAM} GB and ROM is {ROM} TB"
#I forgot the RAM of the system, so I will assign ROM first then I will come over to RAM

#print(specifications(ROM=1,RAM=8))

#print(specifications(1,8)) # With positional argument, the values are taken by the index 

#print(specifications(8,ROM=1)) # Using both positional and keyword arguments

#print(specifications(ROM=1,8)) # This would throw up an error as positional argument follows keyword argument

# No matter the frequency of the arguments, the keyword argument always to be passed at last or nothing should be passed after that


'''
Default Argument
While defining a function we need a value to be pre-defined and can be changed as per the wish
for this daefult argument can be used

'''
# One of my friends has dropped his mobile, and wants to calculate the energy it has struck the ground
def potential_energy(mass,height,gravity=9.8):
	hit = mass * height * gravity
	return f'The mobile has struck the ground at {hit} kg m2 /s2'
#print(potential_energy(0.15,6))

'''
Variable length argument
When the user didn't know the length of the variable to be given, this function can be used
placing a * before the formal argument enables it to take indefinite number of actual arguments

'''

def product(first,*series):
	pro = 1
	for i in series:
		pro =  pro * i
		prod = pro
	return pro

#print(product(2,3,4))

'''
Function for using arguments,using a * before the formal parameter, 
allows it to take indefinite number of inputs as a tuple, 
if no value is passed to the parameter the input will be taken as empty 
tuple
''' 
def bahubali(hero,*others):
	print(f'Value passed to the first parameter is {hero}')
	return f'Values passed to the indefinite parameter are {others}'

#print(bahubali('Prabhas','Anushka','Rana','Ramya Krishna'))


'''

Keyword arguments are the one which take in the form of dictionary
it is notated by ** before the name of the formal argument

'''
def film(name,**actors):
	print(f'Value passed to variable hero is {name}')
	print(f'The actors in the film are {actors.keys()}')
	print(f'The character names are {actors.values()}')
	 #return f'Values passed to the dictionary are {actors}'
# Guess the output
#print(film('Bahubali',Prabhas='Bahubali',Rana='Bhallaladeva',Ramya Krishna='Sivagami')) 
'''
May be we should be more vigilant, there is gap after the name of the variable, which is
not accecpted in python
'''

'''def tea():
	return 'Evening'

def coffee():
	return 'Morning'

def prefer(time):
	print(f'I prefer it on {time}')

prefer(tea())
'''

def first_num(a):
	def second_num(b):
		return a+b
	return second_num

def square(a):
	return a**2

def area(square):
	return square

#print(area(square(5)))


def cart(price,item=1):
	print(item, "cost is :" ,price)

'''cart(price="pen")
cart(item="handbag", price=10000)
cart(price=500, item="shirt")'''


def display(price,item='TV'):
	print(f'{item} price is {price}')

#display(9000)


# Variable length argument
def total_cost(x,*y): # Values passed in the y are taken as 
	print("x is",x)
	print("y is",y)
	su = 0
	for i in y:
		su+=i
	print(x+su)

#total_cost(12,24,36,37)

def sum(n1,n2,*n3):
	print(type(n3))
	print(n1*n2*n3)

#print(sum(1,2,123,246))

def myFun(*argsa):
	print(type(argsa))
	for arg in argsa:
		print(arg)

#myFun('Hello Welcome To GeekforGeeks')

dicts = {'name':'python','version':'3.9'}

#(dicts.keys())

def new(n1,**n2):
	print(n2.keys())
	return n2

#print(new(1,'nothing'))
#print(new(1,name='nothing'))


def sums(a,b):
	return print("Hello World")
	print('hello')

#sums('an','f')

def check(nu):
	if nu%2==0:
		print('even')
	else:
		print('odd')
	return "Gowrav"

#check(12)


def m():
	print("Nothing")
#m()

def sums():
	print('old')

def new():
	print('new')
	sums()
#new()

#
def sum(n1,n2):
	return n1+n2, n1*n2

#print(sum(4,5))

new = sum

'''print(sum(4,5))

print(new(4,5))

print(id(sum))
print(id(new))'''


def shout(text):
	return text.upper()


def greet(func):
	greeting = func("Hi")
	print(greeting)

#greet(shout)


def sum(a,b):
	return a+b,a-b

def mul(a,b):
	return a*b

def combi(func):
	sum1 = func(10,20)
	print(sum1)

#combi(sum)
#combi(mul)


def first(a):
	def second(b):
		return a+b
	return second

adv = first(10)

#print(adv(12))


def roger():
	pass 
roger() # pass is used only when we want to use this function in future 

def note():
	return "Welcome to my world!"

note() # No Result due to no output function

# calling the function without the given name
def ring():
	print("This function is called")

#call() # Results in error as not defined

def gowrav():

	return print("This is my Arena!",end='\t') # This is the end
	print('No Trespassing!')

#gowrav() # returns the first print statement alone as the other is
#return condition, hence return condition exits the function


# Functions performing operations
def full(a,b):
	print(f'The product of {a} and {b} is {a*b}')
	print(f'The addition of {a} and {b} is {a+b}')
	print(f'The subtraction of {b} from {a} is {a-b}')
	print(f'The exponential of {a} raise to {b} is {a**b}')
	print('The product of {} and {} is {}'.format(a,b,a*b))


#full(2,3)

#full(2) # This throws the error the arguments passed are less than the required


def note_display():
	return print("Welcome to my world!") 

#note_display() # Return the statement in the print function

def test_display():
	return 'Suswagatham!'  

variable = test_display()

#print(variable) 


def sums(a,b):
	return print(a+b) 

#sums(4,5)


def movie_review(rating):
	if rating <= 5:
		return print('Avoid at all costs!')
	elif rating > 5 and rating < 9:
		return print('This one was fun.')
	else:
		return print('Outstanding!')

#movie_review(3)

# Calling one function from other

def first(a):
	return print(f'Square of {a} is {a**2}')

def second(a):
	print(f'Cube of {a} is {a**3}')
	first(a) # out of block

#second(4)


# Everything that saved as .py is called module

#from func_args import *

#print(potential_energy(0.5,5))

# Group of modules is called library

# Package is the collection of modules which has __init__ file in it

# Library is a collection of packages



## Local Variable and global variable

def sum(x,y):
	num1=23
num1 = 23
def wish():
	print(num1)
wish()