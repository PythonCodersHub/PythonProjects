age = int(input())
if 13<=age<=19:
    print("Teen")
else:
    print("Invalid Input")


inp = input("Enter anything:")
print(type("The class of input entered is ",inp))
'''

num = input("Enter the age:") # 25
print(type("Input entered is of the class",num)) # string
print(type(int("Input entered is of the class after changing is :",num))) # num


random  = input("Enter something arbitrary") # hello
type_conversion = int(random)

print(type(type_conversion))  

This will throw an error as the entered is string and it cannot be converted to int
A string of int class can be entered to int , but a str of str class cannot be converted to int

# float to int conversion

arb = input('Enter a string  ending with decimals: ') # 250.5
print(type("Intial class of arb is ",type(arb)))
print(type(int("Class of converted value is",arb))) # output is int 
print(arb) # 250 as we converted this to int only value before . are released

# int to float
floe = int(input('Enter a floating value :')) # 25.05'''
#print("Class of the entered variable is :",floe) # This throws an error as the entered value is a float'''

#print(bin(3))'''