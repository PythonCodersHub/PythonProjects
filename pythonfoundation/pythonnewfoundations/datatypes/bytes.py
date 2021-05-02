x = [10,20,30,40,50]
y = bytes(x)
print(y)
print(type(y))

# Accessing the elements in the 

x = [10,20,30,40,50,60]
y = bytes(x)
print(y)
print(y[0])
print(y[1])
print(y[2])
print(y[3])
print(y[4])

# using the loops
x = [10,20,30,40,50,60]
y = bytes(x)
print(y)

for a in x:
    print(a)
    
#ranges or values mst be 0,256
# bytes r immutable
x = [10,20,30,40,50,60]
y = bytes(x)
y[0] = 330
print(y) 
    
    
    