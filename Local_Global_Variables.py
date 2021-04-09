# Local variable and global variable

a = 1

def m1():
	global a # Changing the global value
	b=23 
	print("a valuefrom m1() function",a)
def m2():
	print("a value from m2() function",a)

#m1()
#m2()

num1 = 100
def sum(a,b):
	global num1
	num1=234
	print('num1 value for num1',num1)

def mul(c,d):
	print('num1 value for num1',num1)

#sum(10,20)
#mul(10,20)


# Accessing local and global variables using globals() inbuilt function

a=1
def m():
	a=20
	print(a)
	print(globals()['a'])

#m()


num1 = 900
def add(x,y,z):
	num1 = 'ganguly'
	print('sum of three numbers is ',x+y+z)
	print(num1)
	print(globals()['num1'])

#add(3,4,5)



def facts(n):
	if n==0:
		result =1
	else:
		result = n * facts(n-1)
	return result

x = facts(6)
#print(x)


def fa(x):
	n=4
	s = 1
	while(n>0):
		s = s *n
		n-=1
	return s
#print(fa(4))



# Lambda functions also called anonymous functions

x = 100
x = 'python'
#print(x)
'''import gc
gc.enable()
'''

# lambda is the keyword, n1,n2 are the arguments, n1+n2 are online expression

sums = lambda n1,n2:n1+n2
x =sums(2,32)

#print(x)


# Filter
# Used to filter values from a sequence of values

real = [i for i in range(1,11)]
out = list(filter(lambda i:i%2==0,real))
#print(out)


# Map function, Mapping a particular function onto to the sequence of the elements

multi = list(map(lambda i:i*2,out))
#print(multi)

# Reduce function, reduces the sequence of elements into a single element by applying a specific condition
from functools import reduce

tools = [i for i in range(10)]
new = [i for i in range(11,13)]
#total = reduce(lambda x,y,z:x+y+z,tools,new)
#print(total)




# Decorator
# Special function which add some extra functionality to an existing function

def sums(addition):
	def inner(x,y):
		if x<0:
			x=0
		if y<0:
			y=0
		return addition(x,y)
	return inner
#@sums
def addition(a,b):
	res = a+b
	return res

addition = sums(addition)

print(addition(20,-30))
print(addition(-10,5))



def decor(func):
	def inner_function(x,y):
		if x<0:
	 		x = 0
	 	if y<0:
	 		y = 0
 		return func(x,y)
	return inner_function
@decor
def sub(a,b):
	res = a - b
	return res
print(sub(30,20))
print(sub(10,-5))

