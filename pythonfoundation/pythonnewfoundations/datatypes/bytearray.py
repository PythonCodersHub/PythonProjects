x = [10,20,30,40,50,60]
y = bytearray(x)
print(y)
print(type(y))

# accesing elements
x = [10,20,30,40,50,60]
y = bytearray(x)
print(y[0])
print(y[1])
print(y[2])
print(y[3])
print(y[4])
print(y[5])

x = [10,20,30,40,50,60]
y = bytearray(x)

for a in x:
    print(a)
    
#mutable
x = [10,20,30,40,50,60]
y = bytearray(x)
print("Before modifying ", y[1])
y[1] = 80
print("after modifying ", y[1]) 
print(y)