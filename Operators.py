
# Unary operator , involves only one operands
hit = 7
print(-hit)
# Binary Operator,  involves only two operands
miss = 3
print(hit+miss)
#Ternary operator ,  involves only one operands
div = 23
quo = 4
rem = 5
divi = (div * quo)  + rem
print(divi)

print("-"*150)
#------------------------------------------------------------------------------ Arithmetic Operators------------------------------------------------------
print('Arithmetic Operators')

print(f"The addition of {hit} and {miss} is {hit+miss}") # Addition 

print(f"The subtraction of {hit} and {miss} is {hit-miss}") # Subtraction

print(f"The Multiplication of {hit} and {miss} is {hit*miss}") # Multiplication

print(f"The Float Quotient of {hit} divided by {miss} is {hit/miss}")# Returns the Quotient in float

print(f"The Modulues or Reminder of {hit} divided by  {miss} is {hit%miss}") # Returns the residue of the divison

print(f"The Exponential of {hit} raised to  {miss} is {hit**miss}") # Number raised to its exponential

print(f"The Interger Quotient of {hit} divided by {miss} is {hit//miss}") # Returns the Quotient in integer

print("-"*150)
#  -------------------------------------------------------------------------------------Relational Operators----------------------------
# Used in comparision of two values, returns True if the condition is satified, else False
print('Relational Operators')
car = 4
bike = 2

print(car>bike) # True
print(car>=bike) # True
print(car<=bike) # False
print(car<bike) # False
print(car==bike) # False 
print(car!=bike) # True

print("-"*150)
#------------------------------------------------------------------------------------------- Logical Operators------------------
print('Logical Operators')
low = 2
med = 45
high = 99
some = None
'''
Consider A and B
OR operator returns A if A is True, else returns A is not-false
AND operator returns A is A is False, else returns B if A is not false
NOT operator returns TRUE if the value passed is 0,None,False else returns FALSE  '''


print(low and high and med) #45
print(high or med or low) # 99
print(not some) # True
print(low and low) # 2

print("-"*150)

#-------------------------------------------------------------------------------------------Assignment Operator-----------------------------------
print('Assignment Operator')

speed = 25
for i in range(10):
    print(i+5)
# Assigning + symbol to it increments it by 5
dam = 45
dam+=5
print(dam) # 50

#-------------------------------------------------------------------------------------------Unary Minus Operator-----------------------------------
print('Unary Minus Operator')
# Unary Minus: To change a positive into negative and inverse

neu = complex(4,5)
print(-neu) # -4-5j

newt = -5
print(-newt) # 5


# -------------------------------------------------------------------------------------------Membership Operator-----------------------------------
print('Membership Operator')
#Membership : Used to check whether a element is present or not
text = "Good Day!"
print("Good" in text) # True

flash = "Good Day Lads! Let's nosh together"
if 'Lads' in flash:
    print('Bingo!')
else:
    print('Negative')
#-------------------------------------------------------------------------------------------Identity Operator-----------------------------------
print('Identity Operator')
#Identity'''