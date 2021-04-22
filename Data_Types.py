'''Type'''
string = "Wars"
print(type(string))
integer = 2020
print(type(integer))
decimal = 11.21
print(type(decimal))

compel = 2 + 5j
print(type(compel))

lists = [2,3,24,'Dun',['a','b','c']]
print(type(lists))


home = [0,26,78,190,255]
byte = bytes(home)
print(type(byte))

bytearrays = bytearray(home)
print(type(bytearrays))

dictionary = {"Name":"Bobby","Year":2020}
print(type(dictionary))

tuples = (1,2,3,"Yup",["Hello"])
print(type(tuples))

boo = True
print(type(boo))
print("-"*100)

'''Numeric Types
1. int
2. Float
3. Complex
'''
#------- int ---------
num = 23.4
new_num = int(num)
print(type(new_num))

#---------------------------------------------------------- Float ----------------------------------------------------------
floe = 23.6748

print(type(floe))

# Limiting the decimal values using round function
print(round(floe,2))

# --------------------------------------------------------- Complex --------------------------------------------------------

compel = 2 + 5j
print(type(compel))

compel_auto = complex(3,7)
print(compel_auto)
print(type(compel_auto))

# To winkle real number present in complex
print(compel.real)
# To winkle imaginary number present in complex
print(compel.imag)

print("-"*100)
'''Bool
This operator returns False if there's no assignment to the given variable
If the values assigned are 0,False and None bool operator will throw False as output
'''
coy = []
print(bool(coy))

rant = 'Toodles'
print(bool(rant))

brill = [None]
'''This one results in True as None as considered as an element in the list
From this it can be the exceptions when appended to a list or tuple it becomes a element and the value
passed to the variable is not empty.
'''
print(bool(brill))

# None 

#----------------------------------------------------------- String--------------------------------------------
# Strings play a very important role in analyzing text data.
# Text data can be:
# 1. documents (web, txt, word, pdf)
# 2. in a column of a table where you extract all the information

# Strings are a list of characters

# 1. create a string and subset
# 2. Get the length of a string
# 3. Slicing strings
# 4. Iterating strings
#     a. count the charecters
#     b. find if an charecters is in a string
# 5. Strings are immutable
# 6. using in operator with strings
# 7. comparing strings
# 8. String methods
word = ''
word[0]


word[-1]

len(word)
#Slice the list
word[3:6]
word[2:]
#Iterating on lists
word=['my','name is bond','zh','wht']
print(max(word))
for char in word:
    print(char)

count =0
for char in word:
    count = count+1
print(count)

new='my name is bond'
sc=str(input())
y='n'
for lines in new.split():
    if lines==sc:
        y='o'
        break
if y!='n':
    print('Found')
else:
    print('Not Found')






line='python is interesting'
lin=str(input("enter the word"))
found='no'
for i in line.split():
    if i==lin:
        found='yes'
        break
if found!='no':
    print('Found')
else:
    print('Error')

# in operator
search_char = 'l'
if search_char in word:
    print(search_char, " Present in the word")
else:
    print(search_char, " Not present in the word ")
#Strings are immutable
word[3] = 'z'
# for Multi lines use \n
# \n - new line charecter
multi_line = 'welcome to the course on python\ni am linking the course\ni am enjoing python'
print(multi_line)
# String Methods
#  1. startswith
#  2. endswith
#  3. isupper, upper
#  4. islower,lower
#  5. istitle, title, capitalize
#  6. isalpha
#  7. split
#  8. splitlines
#  9. join
#  10. strip
#  11. rstrip, lstrip
#  12. find
#  13. rfind
#  14. replace
#  15. count

word = "Python Programming"
print(word.startswith("Pyt")) #check for multiple char's
print(word.startswith("p")) #cehck for a single char

word = "Have a nice day"
print(word.endswith("day"))
print(word.endswith("i"))
word = "python"
print(word.isupper())
print(word.upper())


# islower - checks if all the charecters are in lower case
# lower - converts the string to lower case
# islower - checks if string is in title case (i.e first charecter is in upper case)
# lower - converts the string to title case

line = "Affluent British Culture"
line.title()
for i in line:
    if line.islower():
        line.Upper()
print(line)

#Capitalize the first letter
line.capitalize()
print("Hello".isalpha())
print("He11o".isalpha())
#Split by space by default
text = "Welcome to my Arena"
print(text.split())

#Split by the specified character
text = "welcome,to,my,arena"
print(text.split(","))

text = "Date 23 07 2019"
print(text.split(" ",1))
#obtain date from the text
print(text.split(" ",1)[1])

multi_line = 'welcome to the course on python\ni am linking the course\ni am enjoing python'
print(multi_line)

print(multi_line.splitlines())

print(multi_line.splitlines(True))

# use list comprehension to remove the \n
print([ line.strip() for line in multi_line.splitlines(True)])

#When you have a multiple lines, and you use split. how do you eliminate the \n
print(multi_line.split("\n"))

''' White space charecters
 ' ' – Space
 '\t' – Horizontal tab
 '\n' – Newline
 '\v' – Vertical tab
 '\f' – Feed
 '\r' – Carriage return
 Strip removes white space characters'''

word = ["Hang on",'525']
print(word)

word = " Hang on\t"
print(word)
print(max('what','whatwhat','is','python'))

print(word.strip())

print(word.rstrip())

print(word.lstrip())

print(word.find("l"))

print(word.rfind("l"))
#Replace all occurrence
line = "I am not interested. i am not in a position"
line.replace("not ","")

''' strip -> removes the charecter beginning and at end
replace -> replaces the charecter with another charecter anywhere in the string'''

word = "Doodle doo"
print(word.count("p"))

#converting string into list
print(list(word))
print(word.split(" "))

date = "Today's Date is 23 07 2019"
date.split(" ",3)[3].replace(" ","-")
# Find if the line starts with a word
multi_line = 'welcome to the course on python\ni am liking the course\ni am enjoying python'
print(multi_line)
print([line for line in multi_line.splitlines() if line.startswith('welcome')])

#Finding the frequency of occourrence of character
word = "renaissnce"
wc = []
for char in word:
    wc.append((char,word.count(char)))
wc.sort()

print("-"*100)
# ----------------------------------------------------------------bytes--------------------------------------------------------------
new_list = [1,2,34,56,78,356,356]
byte_list = bytes(new_list)
print(byte_list)
# Above will result in an error as the value ranged above 255
mod_list = [3,23,56,42,87]
byte_lists = byte(mod_list)
byte_lists[2] = 56
print(byte_lists)
# THe above results results in error as the byte are mutable

# ---------------------------------------------------------------Bytearray-------------------------------------------------
new_list = [1,2,34,56,78,356,356]
byte_list = bytearrays(new_list)
print(byte_list)
# Above will result in an error as the value ranged above 255
mod_list = [3,23,56,42,87]
byte_lists = bytearrays(mod_list)
byte_lists[2] = 56
print(byte_lists)
# THe above results will be executed and bytearrays are immutable
# ---------------------------------------------------------------Tuple------------------------------------
tips = (1,1,1,1,1,1,1,"oy",'oy','oy','oy','oy','oy',"Oy","Oy","Oy","Oy",2,3,["How are you?","I'm bloody starving"])
print(tips.index(2))

scrap = ('Muster')
print(type(scrap))
# The above is returns a string even though it's enclosed in braces, this is due to abscence of comma
# To find the frequency of a specific value
print("Frequency of word oy is",tips.count('oy'))
# ------------------------------------------------------------------list-----------------------------------------------
lass = [2, 'a', 4.5, False]
print(lass)
print(lass[1])

# Slicing a list
myList = [3.44, 44.34, 23.23, 32.1, 35,46,69,70]

print(myList[0::2])

print(myList[-7:-2]) #[inclusive index : Exclusive index]
print(myList[3::5])

print(myList[:6])

print(myList[-1])

print(myList[-8:-5])
# Search element in a list

print(3.44 in myList)


if 3.44 in myList:
    print('element found')
else:
    print('element not found')

myList1 = list() #similar to assigning to []
myList1.append([10,32])
myList1.append(20)
myList1.append(30)
myList1.append(40)

print(myList1)

print(myList+myList1)

print(myList.reverse())

print(myList1*3)

print(myList.index(35))

print(myList.index(100))

emp_names = ["Mohan","Madhu","Raghu","Priya"]
emp_salaries = [5000,6000,2500,6000]
name = "Raghu"

old = [10,20,'hi','hello',4.5,9.5]
new = old

print(old)
print(new)

old[5] = 2000
print(old)

print(new)

print(id(old))

print(id(new))
''' Conclusion : Both x and y will contain the same data, will refer to the data location in memory.
y = x, will result in shallow copy of the elements of x into y, which means y is an alias to x
any changes to x reflect in y and any changes to y refect in x'''

print(type(old))
#All the mehods of the list class. 
# Lists all the operaions which can be applied on lists

update = old.copy() # it creats a new copy or a deep copy and stores it in z

print(update)

up_date=update.reverse

old[2] = "good morning"

print(old)

print(update)

print(id(old))

print(update)


''' Conclusion :  x and z will contain the same data, will refer to the different locations in memory.
z = x.copy(), will result in deep copy of the elements of x into z, which means that all the elemnts in x will be copied to a different location in memory
x and z are 2 independent copies
any changes to x will not reflect in z and vice versa

 list menthods
 1. list()
 2. append()
 3. extend()
 4. index()
 5. copy()
 6. remove()
 7. pop()
 8. reverse()
 9. sort()'''

#1. list() - creates a list. with no aruments, creats an empty list
new = list([10,20])
print(new)

rind=[1,'ab',3]
print(rind*2)

# 2. append - add an element into the list
new.append(old)

#append can also be used to add multiple elements. which will be added as a sub list
new.append([40,50])
print(new)

# 3. extend() - concatenates two lists
new=[10,20,30]
old = [100,200,300]
new.extend(old)
print(new)

#pop() - remove the element by specifying the index
print(new.pop(1))

#pop without any arguments removes the last element
print(new.pop())

#remove() - remeove, by specifying the value of the element
print(new.remove(30))

lis = [5,6,7,8,2,3,0]

print(lis.count(3))
#reverse() : prints the elements from last to first
print(new.reverse())

print(new.sort())

print(new.reverse())

print(new.insert(4,3))

print(new)
# A combination of sort and revrse, will result in the list in descending order

print(len(new)) # find the length of any collection

old = [100,200,2,2,3,55,6,8,8,9,10,-50]

print(len(set(old)))

print(len(old))

#set method removes duplicate elements from the list 
# and it also  sorts the list in increasing order
old_set = set(old)
print(old_set)

print(help(old))

# Equivalent and identical lists are those created with shallow copy
# After your deep copy(using .copy()), the two lists are equivalent and not identical

#help(x) - details about all the methods of object x
#dir(x) - lists all the methods of object x

print(new.count(8))


#------------------------------------------------------------------ range -------------------------------------------------------
for i in range(4):
    print(i**2)

print(list(range(10))) #list from 0 to 9
print(list(range(1,5))) # list from 1 to 4
print(list(range(1,10,2))) # from 1 to 9 in step of 2

#-------------------------------------------------------------------------set----------------------------------------------------
rand = [1,1,2,3,4,5,6,7,8,9,9,9,9,9,10,11,]
print(len(rand))
print(len(set(rand)))

# Adding an element to set
colours = {"red","blue","green"}
colours.add("yellow)
print(colours)

# To clear all the elements in the set
print(colours.clear())

# Set difference returns only the elements present in the list compared to the other list
prim = {'one','two','three'}
co_prime={'two','three'}
diff = prime.difference(co_prime)
print(diff)

# Discarding an element
colours = {"red","blue","green"}
colours.discard("blue")
print(colours)

# Set intersection returns the items existed in both the sets
prim = {'one','two','three'}
co_prime={'two','three','four'}
combi = prim.intersection(co_prime)
print(combi)

# Intersection update returns the common elements by removing the uncommon elements in it
sham = {1,2,3,4,5,6}
flam = {3,4,5,6,7}
sham.intersection_update(flam)
print(sham)

# Disjoint Function - returns True if there is no common element , else False
sham = {1,2,3,4,5,6}
flam = {3,4,5,6,7}
bam = sham.isdisjoint(flam)
print(sham)

# Subset function - returns True if all the elements in the subset of the other set
sham = {1,2,3,4,5,6}
flam = {3,4,5,6}
res = flam.issubset(sham)
print(res)

# superset function - returns whether the comparitive is superset of the other
sham = {1,2,3,4,5,6}
flam = {3,4,5,6}
super_set = flam.issuperset(sham)
print(super_set)

# Pop argument chucks a random element, it's is most likely the first element in the set
spin = {1,2,4,56,78,43,46,223,556}
spin.pop()
print(spin)

#Remove - unlike pop it can remove a certain element which is known
chuck = {1,2,4,56,78,43,46,223,556}
chuck.remove(56)
print(chuck)

# Symmetrics Difference Update- removes the element in both the sets and returns the other elements present
prme = {2,3,5,7,11}
whole = {0,1,2,3,4,5,6,7,8,9,10,11,12}
sym_diff = whole.symmetric_difference_update(prme)
print(sym_diff)

# union - to combines the sets and returning only the unique elements in the sets
soap = {3,4,5,6,7,8,9,10}
mop = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,34}
uni = soap.union(mop)
print(uni)

# Set Update, updates set with the new elements found in the other set
mini = {3,4,5,6,7,8,9,10}
maxi = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,34}
mini_max = mini.update(maxi)
print(mini_max)


print("*"*100)
#----------------------------------------------------------------------- dict ---------------------------------------
emp = {"Mohan":5000,"Madhu":6000,"Raghu":2500,"Priya":6000}
#fetching the salary of employee Priya
print(emp["Priya"])
#Adding a new key value
#If a key is not existing, then the below will add the key and the value
# to the dictionary
emp["Shankar"] = 60000
print(emp)
#updating values for existing keys
emp["Raghu"] = 40000
print(emp)
#creating an empty dictionary
empty_dict = {}
emp_dict = dict()
#Extracting the keys and values from dictionary
print(list(emp.keys()))
print(list(emp.values()))
#iterating dictionaries, means iterating on keys
for elem in emp:
    print(elem, emp[elem])
#Get me the name, salary, and bonous on salary which is 10% on the salary
#math to compute final salary after applying bonous
salary = 5000
bonous = salary * (10/100)
print(bonous)
final_salary = salary + bonous
print(final_salary)
for elem in emp:
    print(elem,emp[elem],round(emp[elem]*1.1,2))
#Get me the names of employees who earn more than 5000
#Fetch the keys where the values are > 5000
for elem in emp:
    if emp[elem] > 5000:
        print(elem)
[elem for elem in emp if emp[elem] > 5000]
#Subsetting a dtict on non existiant key, results in an error
print(emp['Rama'])
'''
check if the key is present, if so print the vlaue
else, print 'employee not found'
'''
print(emp.get('Rama','Employee not found'))
print(emp.get('Raghu','Employee not found'))
print(emp.get('Rama'))

'''Dictionaries are mutable collection of heterogenous elements (called as values)which have named indexes.
dictionaries allows me to define indexes(called as keys), rather than using predefined indexes
keys cannot be duplicated, but values can be duplicate'''
emp1 = {"Mohan":5000,"Mohan":6000,"Raghu":2500,"Priya":6000}

print(emp1)
# Sorting dictionaries

# Sorting on keys:
#     1. Take the keys and convert to a list
#     2. sort the list
#     3. iterate the dictionary based on the sorted order of the list
emp_keys = list(emp.keys())
emp_keys.sort()
emp_keys
#For every element in the sorted list of keys
#fetch the key and the value from the dictionary
for elem in emp_keys:
    print(elem,emp[elem])
print(list(emp.items()))
# When a dictionary is converted to a list, then we get a list of tuples

print("Done!")