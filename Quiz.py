
# Take a list of numbers
print("In Which Year did the Titanic Ship sunk ? ")
count = 0
chances = int(input("Enter number of Chances you wanna try for the question : ")) # An user input function to enter the number of chances to try the question
Year = 1912 # Solution
if chances<=5: # If the entered chances is more than 5 it opens this loop
    print("Hint: It's two years before World War I")
    # To allow the user to enter number of times he want to enter the choices we call this range function
    for i in range(chances):
        count+=1 # this is count number of times the user has entered
        enter = int(input(f"Guess no.{count}: ")) # Taking the input from user
        if enter==Year: # True Statement of the loop
            print("Bingo! You possess great knowledge !")
            break       
        else: # If the answer is wrong we prompt the user to see the number of choices left
            if chances-count>0: # To know whether the user is near another if-loop is present
                if 1909<enter<1915:
                    print(f"You are near buddy ! You have {chances-count} chances left !")
                else:
                    print(f"You are far away ! You have {chances-count} chances left !")
                
            else: # If the chances are over this will be the message \U0001f600 is the code for emoji
                print("Out of chances of buddy ! Sometimes you need to notice the years in films :) \U0001f600 ")       
else:
    print(" I can't give you no more than 5 chances !")

print("-"*100)
print("Enter a list of numbers get whether the number is prime or Composite")
lsts = [int(i) for i in input("Enter the numbers seperated by a space: ").split(" ")]
res = []
for num in lsts:
	if num > 1:
	   for i in range(2,num):
	       if (num % i) == 0:
	           res.append("Composite")
	           break
	   else:
	       res.append("Prime")
	else:
	   res.append("Invalid")
print(res)
print("-"*100)

# Addition of first n numbers
print("Getting the sum of first n number")
number  = int(input("Enter the number for adding the numbers :"))
su = 0
for i in range(0,number+1):
	su = su + i
print("Addition of first",number," numbers is",su)

# Factorial of the number 
start = 1
number = int(input("Enter the number for factorial :"))
su = 1
for i in range(1,number+1):
	su = su * i
print("Factorial of",number,"is",su)

print("-"*100)

num =5
fact = 1
count = 1
while num>=1:
	fact = fact * num
	num-=1
print(fact)

print("-"*100)

print("Input the number of students and marks of subjects and get the grade for it")
 
NoOfStudents = int(input("Enter the number of students:"))
count = 1
while count<=NoOfStudents:
	marks1 = int(input("Enter the marks of subject 1 :"))
	marks2 = int(input("Enter the marks of subject 2 :"))
	marks3 = int(input("Enter the marks of subject 3 :"))
	average = (marks1+marks2+marks3) / 3
	if average>65:
		print(" Grade A")
	else:
		print(' Grade B')
	count+=1

number = int(input("Enter a number :"))
pas = []
for i in range(1,number+1):
	pas.append(i )


print("Well Done !")