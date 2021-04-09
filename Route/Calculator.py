# Taking the input from the given output
def addition(first,*rest):
	next =0
	all = [] # Using list to display all the inputs in a single section
	all.append(first) # Appended the first element a
	for i in rest:
		all.append(i)# Appending the tuple elements to list
		next+=i
	return f"The sum of the provided numbers {all} is {first + next}"	

def product(first,*rest):
	prod = 1
	all = []
	all.append(first)
	for i in rest:
		all.append(i)
		prod*=i
	return f'Product of the provided numbers {all} is {first*prod}'

def divide(first,second):
	return f"{first} divided by {second} is {first/second}"

def root(first,second):
	return f"The {second} root of {first} is {first**(1/second)}"

def factorial(number):
	start = 1
	for i in range(1,number+1):
		start*=i
	return f'Factorial of {number} is {start}'

def exponential(number,power):
	return f'{number} raised to exponent {power} is {number**power}'




