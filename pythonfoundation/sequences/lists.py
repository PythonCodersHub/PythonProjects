# Python lists are similar to an array but they allow us to create a heterogeneous collection of items inside a list.
#A list can contain numbers, strings, lists, tuples, dictionaries, objects, etc.
# Lists are declared by using square brackets around comma-separated items.
# Lists are mutable which makes it easier to change and we can quickly modify a list by directly accessing it.

# lists = [1,2,3,4]
# print(lists)

# bikes =['Alfa', 'Cbz', 'honda', 'harleydavidson', 'ninja']
# print(bikes)

# Creating lists with elements
# cricketers = ['ck', 'db', 'La', 'Ma', 'VM', 'SG', 'KD', 'ST']
# print(cricketers)

#Accessing elements
# bikes =['Alfa', 'Cbz', 'honda', 'harleydavidson', 'ninja']
# print(bikes)
# print(bikes[0].title())
# Lower Upper cases
# bikes =['Alfa', 'cbz', 'honda', 'harleydavidson', 'ninja']
# print(bikes[0].title())
# print(bikes[0].upper())
# print(bikes[1].upper())
# print(bikes[2].upper())
# print(bikes[3].upper())
# print(bikes[4].upper())

#indexpositions
# bikes =['Alfa', 'Cbz', 'honda', 'harleydavidson', 'ninja']
# print(bikes[0].title())
# print(bikes)
# print(bikes[0])
# print(bikes[1])
# print(bikes[2])
# print(bikes[3])
# print(bikes[4])
#negativeindexing
# print(bikes[-1])
# print(bikes[-2])
# print(bikes[-3])
# print(bikes[-4])

# concatenation
# bikes =['Alfa', 'Cbz', 'honda', 'harleydavidson', 'ninja']
# message = ("My first bike was" +bikes[0].title()+ ".")
# print(message)

# modifyinglist
# The bikes list display the original list with Alfa as the first element
# bikes =['Alfa', 'Cbz', 'honda', 'harleydavidson', 'ninja']
# print(bikes)
# the bikes[0]= ducati changes the first item ie replacing the Alfa to ducati
# the first item in the list changes and rest remains same
# bikes[0] = 'ducati'
# print(bikes)

# Appending
# the simple way to add elements in the list is appending
# whenever a new element is added or appended it is added at the end
# bikes =['Alfa', 'Cbz', 'honda', 'harleydavidson', 'ninja']
# print(bikes)
# bikes.append('ducati')
# print(bikes)

# emptylists

# bikes = []
# bikes.append('Yamaha')
# bikes.append('HeroHonda')
# bikes.append('Ninja')
# print(bikes)

# l1 = []
# print(l1)
# print(type(l1))

# inserting the element with index
# This method allows to insert the element at the appropriate index
# bikes =['Alfa', 'Cbz', 'honda', 'harleydavidson', 'ninja']
# print(bikes)
# bikes.insert(4 , 'Tomcat')
# print(bikes)

# Removing the elements from the list
# bikes =['Alfa', 'Cbz', 'honda', 'harleydavidson', 'ninja']
# print(bikes)
# del bikes[4]
# print(bikes)

#Popmethod()
# bikes =['Alfa', 'Cbz', 'honda', 'harleydavidson', 'ninja']
# print(bikes)
# poppedbikes = bikes.pop(4)
# print(poppedbikes)

#poppedlist
# bikes =['Alfa', 'Cbz', 'honda', 'harleydavidson', 'ninja']
# print(bikes)
# last_owned = bikes.pop()
# print(" last owned bie was"+last_owned.title()+".")

#sorting
#Sorting the list permenantely
# cars=["benz","audi", "bmw", "ford", 'ferrari']
# print(cars)
# cars.sort()
# print(cars)
#sorting the list in the reverse direction
# cars=["benz","audi", "bmw", "ford", 'ferrari']
# print(cars)
# cars.sort(reverse=True)
# print(cars)

# Sorting the temporary lists with sorted functions
# cars=["benz","audi", "bmw", "ford", 'ferrari']
# print("the original list is", cars)
# print(" \n the sorted list is", sorted(cars))

# printing the list in the reverse order
# cars=["benz","audi", "bmw", "ford", 'ferrari']
# print(cars)
# cars.reverse()
# print(cars)
# Length of the cars
# cars=["benz","audi", "bmw", "ford", 'ferrari']
# print(cars)
# print(len(cars))
# print(type(cars))

# Working with lists
# Looping trough the list
# cricketers = ['Col CK', 'Bradman', 'Sachin']
# for cricketer in cricketers:
#     print(cricketer)
# doing extra work    
# cricketers = ['Col CK', 'Bradman', 'Sachin']
# for cricketer in cricketers:
#      print(cricketer.title() + ", is the greatest of all generations") 
#      print("The greatest legend of all the time is ," +cricketer.title()+".\n" )   
# print("thank you fir the voting and declaring the positive result")     
# Accessing trough loops
# a = [100,200,300,400]
# for b in a:
#     print(b)
# whileloops
# a = [100, 200, 300, 400]
# b = 0
# while b<len(a):
#    print(a[b]) 
#    b = b+1

#range function
# for a in range(1,5):
#     print(a)
# print("\n newline")    
# for b in range(1,6):
#     print(b)    

# Making the list using the range function
# num =list(range(1,12))
# print(num)

# evennumbers
# even_num = list(range(2,16,2))
# print(even_num)

#odd numbers
# odd_num = list(range(1,15,2))
# print(odd_num)

#squares of numbers
# squares = []
# for i in range(1,15):
#     square = i**2
#     squares.append(square)
#     print(squares)

# cube of numbers
# cubes = []
# for a in range(1,20):
#     cube = a**3
#     cubes.append(cube)
#     print(cubes)
# a =  []
# a.append('1')
# a.append('2')
# a.append('3')
# print(a)



# Creation of list using the range  
# a = range(1,20)
# b = list(a)
# print(b)
# List comprehension 
# squares = [i**2 for i in range(1, 20)]
# print(squares)      
# cubes  =[a**2 for a in range(1,20)]
# print(cubes)   

# Slicing list

# players = ['CK', 'DB', 'LA','Tiger', 'Master', 'LM' ]
# print(players[0:5])
# print(players[0:4])
# print(players[0:3])
# print(players[0:2])
# print(players[0:1])
# print(players[1:0])
# print(players[1:2])
# print(players[1:3])
# print(players[1:4])
# print(players[1:5])

# print(players[2:0])
# print(players[2:1])
# print(players[2:2])
# print(players[2:3])
# print(players[2:4])
# print(players[2:5])
# print(players[:4])
# print(players[4:])
# print(players[:3])
# print(players[3:])

# looping trough slices
# print("The best players of my team are :")
# for player in players[:3]:
#     print(player.title())
    
#copying lists
# my_games = ['C', 'CS', 'CDS', 'IGI']
# friend_games = my_games[:] 
# print(my_games)
# print(friend_games)

# creating list using the list() function

# b = range(1,21)
# a = list(b)
# print(a)
# print(type(a))

# Mutability
# a = [1,2,3,4,5]
# print(a)
# print("Be fore modifying", a[0])
# a[0] = 20
# print("after modifying", a[0])
# print(a)

# methods
# n = ['Get', 'set', 'got', 'hello']
# print(n)
# print(len(n))

# count

# b = [1,1,2,3,4,4,5,6,7,7,8,9,10,1,12,12,13,15]
# print(b.count(1)))
# print(b.count(4)))
# print(b.count(7)))
# print(b.count(12))

#extend
# l1 = [1,2,3]
# l2 =['A', 'B', 'C']
# print("Before ext", l1)
# print("before ext", l2)
# l2.extend(l1)
# print("After ext", l1)
# print("After ext", l2)

# alaising
# x = [1,2, 60]
# y = x
# print(x)
# print(y)
# print(id(x))
# print(id(y))
# x[1] = 60
# print(x) 
# print(y)
# print(id(x))
# print(id(y))

# cloning
x = [100, 200, 400]
y = x[:]
print(x)
print(y)
print(id(x))
print(id(y))
x[2] = 600
print(x)
print(y)
print(id(x))
print(id(x))