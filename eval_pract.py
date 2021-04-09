std_inp = input("Enter the first random :") # 12.2
std_inp2 = input("Enter the second random: ") # 2.3
print("Class of rand is ",type(std_inp)) # str
print("Class of rand2 is ",type(std_inp2)) # str
print(std_inp+std_inp2) #12.22.3
# while the above results takes input as a string and prints the concatenation of the two strings passed

rand = eval(input("enter any variable : ")) # 12.2
rand2 = eval(input("enter the other variable : ")) # 2.3

print("Class of rand is ",type(rand)) # float
print("Class of rand2 is ",type(rand2)) # float
print("The addition operation of the passed variables is",rand+rand2) #14.5

'''
#Unlike standard input eval function automates the value of the class and can be used for further implementation
#can be done, using eval function eleminates this conversion and will give the output in a automated manner
'''

# What it might result
print(eval('15 and (5 or None))') # An interesting result might be waiting for you rather than usual
#  Solving an expression using eval() function
exp = eval(input("Enter an expression:")) # 2+3/9%3

print("The value of the expression is: ",exp) # 2.335

# many operations can be performed in the eval function
# make suere that always expression or value passed in the eval should be in inverted commas
print(eval('10 and None')) # Guess what ??
 
exp_2 = eval(input("Enter an expression :"))  # 5 and (None or 15)
print("Entered will be resulting: ",exp_2) # Guess It

new_thing = input("Enter the new expression:")
print("Computed value of system input is :".new_thing)

eval_exp = eval(input("Enter the expression using eval function:"))
print("Computed value of eval function is :",eval_exp)
print('Done!')