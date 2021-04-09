a = 5 
b = 9

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a % b)
print(a*b)
print(a**b)

#comparison operators
x = 6 
y = 9
print(x == y)
print(x!= y)
print(x >  y)
print(x <  y)
print(x >= y)
print(x <= y)
print("\n")
#logicaloperators
c = 6 
d = -6
#and
print(c > 0 and d <0)
print("\n")
#or
print(c > 0 or d < 0)
print("\n")
#nor,\
print(not(c > 0 and d <0))
print("\n")

#identity operators
x = [1,2,3]
y = [1,2,3]

#is
print(x is y)
#isnot
print( x is not y)
print("\n")

#membership operators
teams = ['India', 'Mi', 'csk']
#in
print('csk' in teams)
#notin
print('rec' not in teams)

#bitwiseoperators

x = 0b1100
y = 0b1010

#and
print(x&y)
#or
print(x | y)
#xor
print(x^y)
#not
print(~x)
#leftshift
print(x >> y)
#rightshift
print(x << y)