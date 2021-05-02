#range
for value in range(1, 10):
    print(value)
#using number as variable    
numbers = list(range(1, 100))
print(numbers)    
#evennumber
evennumber = list(range(2,20,2))
print(evennumber)

#oddnumber
oddnumber = list(range(1,25,2))
print(oddnumber)
# Squarenumber
squares = []
for value in range(1,14):
    square = value ** 2
    squares.append(square)
print(squares)    

squares = [value ** 2 for value in range(1, 14)]
print(squares)    

# cubenumber
cubes = []
for value in range(1,14):
    cube = value ** 3
    cubes.append(cube)
print(cubes)  
cubes = [value ** 3 for value in range(1, 14)]
print(cubes)  

powerfour = [value ** 4 for value in range(1, 14)]
print(powerfour)  