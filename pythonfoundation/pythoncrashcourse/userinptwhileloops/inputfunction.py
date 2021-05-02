cric = input("Enter the 4 or 6 and repeat it :")
print(cric)

# Always write clear prompt
name = input("Enter the name :")
print("Hello ," + name + "!")

# using prompt and passing the variable to the input
prompt = "Subscribe to us we can send u the mails of  your subscription"
prompt+="\enter your name"
name = input(prompt)
print("Hello ," + name + "!")

# using the int function
age = input("Enter your age")
age = int(age)
age>=18
print("the age iis", age)

# cal height for roller coster

height = input("ENter the height in inches")
height = int(height)

if height >= 36:
    print("Elgible to ride in a roller coster ride")
else:
    print("\n Come back after some time")
    
print(height)  

# even or odd
number = input("ENter a number")
number = int(number)

if (number % 2 == 0):
    print("the number"+str(number)+  "is even")
else:
    print("The number"+str(number)+  "is odd")    

  