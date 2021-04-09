def sum(a,*b):
	sum=0
	for i in b:
		sum+=i
	return a + sum	

def product(a,*b):
	prod = 1
	for i in b:
		prod*=i
	return a*prod

def factorial(a):
	start = 1
	for i in range(1,a+1):
		start*=i
	return start



