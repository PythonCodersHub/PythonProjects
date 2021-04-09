from sys import argv
'''
One can access the elements in the script using command line arguments 
and the script to be passed should call the arguments
if they are not called in the script there is no point in using the
command line arguments



Open the command prompt from the address bar
and type the filename by passing the arguments
as per the script arguments passed are plugged in
'''

print("The file name is",argv[0])
print("First number entered is :",argv[1])
print("Second number entered is :",argv[2])
# In order to determine the length of the arguements passed through the commands it can be seen through

print("The length of the arguments passed through the command line is ",len(argv)-1)

print("Without conversion the addition of two strings will be as",argv[1]+argv[2])

print("The addition of two numbers is :",int(argv[1]) + int(argv[2]) )

print("The subtraction of two numbers is :",int(argv[1]) - int(argv[2]) )

print("The Multiplication  of two numbers is :",int(argv[1]) * int(argv[2]) )

