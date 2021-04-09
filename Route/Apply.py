# Importing the Route as a package
import Route
# Importing Calculator as sub module in the package
from Route import Calculator,Days,Force,Area

# Calling factorial function from the Calculator Module
print(Calculator.factorial(5)) #Factorial of 5 is 120

# Calling addition function from the Calculator Module
print(Calculator.addition(1,2,3,4,5)) # The sum of the provided numbers [1, 2, 3, 4, 5] is 15

# Calling product function from the Calculator Module
print(Calculator.product(1,2,3,4,5)) # Product of the provided numbers [1, 2, 3, 4, 5] is 120

# Calling Square function from the Area Module
print(Area.Square(7)) # Area of Square with side 7 is 49

# Calling Rectangle function from the Area Module
print(Area.Rectangle(7,8)) #Area of Rectangle with Length 7 and Breadth 8 is 56

# Calling Cube function from the Area Module
print(Area.Cube(7)) #Surface area of Cube is 294


# Calling Alive Days function from the Days Module
print(Days.Alive_Days(1990,1,1)) # You are 11416 days old

# Calling Birthday Days function from the Days Module
print(Days.Birthday_Days(1990,1,1)) # It is 272 days from your birthday

# Calling potential energy function from the Force Module
print(Force.potential_energy(0.15,12)) # Potential energy acting on the particle is 17.65197 J

# Calling kinetic energy function from the Force Module
print(Force.kinetic_energy(0.15,6)) # Kinetic energy acting on the particle is 2.6999999999999997 J
