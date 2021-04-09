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
#     b. find if an characters is in a string
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

# White space charecters
# ' ' – Space
# '\t' – Horizontal tab
# '\n' – Newline
# '\v' – Vertical tab
# '\f' – Feed
# '\r' – Carriage return
# Strip removes white space charecters

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




str1 = "welcome" # 1 is the inclusive index, 7 is the exclusive index if nothing is mentioned after it
# the default stride is 1
print(str1[1:6]) # elcom


squad = "Squadron is on patrol"

print(len(squad)) # 21 here it counts also the spaces

some_thing = "Supreme Leader"
print(some_thing[12]) # indexing method works as usual like of slicing

print(some_thing.upper()) # prints everything in upper case

print(some_thing.lower()) # prints everything in lower case

print(some_thing.isupper()) # returns the boolean value for whether the given string is upper or not

print(some_thing.islower()) # returns the boolean value for whether the given string is lower or not



main ='welcome' # len function results in the number of characters in the given variable

sub = 'elc'

#print(main.rfind('e'))


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

new = ' Hello '

# To remove the spaces
new_2 = new.strip()
print(new)
print(new_2)


well = ' Python '
print("Actual length",len(well))
print("Left Stripped length",len(well.lstrip()))
print("Right Stripped length",len(well.rstrip()))


rand = 'welcome to python programming'
print(rand.rindex('to'))


name = 'Mr.Luke Skywalker'
#print(name.split('.')[1].split(' ')[0])

scrap = 'hello welcome to python : programming language'
print(msg4.split(":")[0].split(" ")[0])



text = "Date 23 07 2019"
print(text.split(" ",1))
#obtain date from the text
print(text.split(" ",1)[1])


profile = ('Hrithik','Roshan','Krish')
movie_star = ' '.join(profile)
pro = 'someThing'
#print(pro.swapcase())

date = "Today's Date is 23 07 2019"
date.split(" ",3)[3].replace(" ","-")
# Find if the line starts with a word
multi_line = 'welcome to the course on python\ni am liking the course\ni am enjoying python'
#print(multi_line)
print([line for line in multi_line.splitlines() if line.startswith('no')])

#Title Method

some = 'Telugu'
a = "hello"
b = "welcome to the jungle"
c = "10.000"

txt = "50.0"

x = txt.zfill(10)
print(len(txt))
print(x)
print(len(x))

exmpl = "How are you ?"
print(len(exmpl))

