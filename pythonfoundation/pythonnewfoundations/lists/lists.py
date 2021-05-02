bicycles = ['Hero', 'Atlas', 'gen', 'well']
print(bicycles)
print(type(bicycles))

# Accessing the elements
print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])
print("\n newline")
# positive indexing
print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])
print("\n")
# ngative indexing
print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-3])
print(bicycles[-4])
# Using Title()
print(bicycles[0].title())

# using individual vlues from the list
bicycles = ['Hero', 'Atlas', 'gen', 'well']
message = "My first bicycle was  "  + bicycles[0].title()  +  "!"
print(message)

# modifying the lists

bikes = ['Hero', 'Harley', 'Ducati']
print(bikes)
print(type(bikes))
bikes[0] = 'hellcat'
print(bikes)
# adding elements to the end of the list
bikes = ['Hero', 'Harley', 'Ducati']
bikes.append('Hellcat')
print(bikes)

# empty list
bikes = []
bikes.append('Hero')
bikes.append('Apache')
bikes.append('Hellcat')
bikes.append('Harley')
bikes.append('Ducati')
bikes.append('Firro')
print(bikes)
# inserting elements into the lists
bikes.insert(6, 'yamaha')
print(bikes)

# Removing the item using del statement
del bikes[0] 
print(bikes) 

# pop method

bikes = ['Hero', 'Harley', 'Ducati', 'Hellcat', 'Yamaha', 'Apache']
popped_bikes = bikes[0]
print(bikes)
print(popped_bikes)

bikes = ['Hero', 'Harley', 'Ducati', 'Hellcat', 'Yamaha', 'Apache']
last_owned = bikes.pop(5)
print("the last bike was  " + last_owned.title() +"!")

# removing an item
bikes = ['Hero', 'Harley', 'Ducati', 'Hellcat', 'Yamaha', 'Apache']
print(bikes)
bikes.remove('Apache')
print(bikes)

# Organising the lists
cars = ['ferrari', 'benz', 'astromartin', 'bmw', 'chevrolet', 'ford', 'honda']
print(cars)
cars.sort()
print(cars)
# reversreorder
cars = ['ferrari', 'benz', 'astromartin', 'bmw', 'chevrolet', 'ford', 'honda']
print(cars)
cars.sort(reverse=True)
print(cars)
# Temporary sorting
cars = ['ferrari', 'benz', 'astromartin', 'bmw', 'chevrolet', 'ford', 'honda']
print("the original list")
print(cars)
print("\n the sorted list")
print(sorted(cars))
# reverse order
cars = ['ferrari', 'benz', 'astromartin', 'bmw', 'chevrolet', 'ford', 'honda']
cars.reverse()
print(cars)

# length of list
cars = ['ferrari', 'benz', 'astromartin', 'bmw', 'chevrolet', 'ford', 'honda']
print(len(cars))

# working with lists
# forloop
cricketers = ['ck','db','vr','sg','st']
for cricketer in cricketers:
    print(cricketer)
    
cricketers = ['ck','db','vr','sg','st']
for cricketer in cricketers:
    print(cricketer.title()   + "  is the greatest cricketer of all time"  + "!")
    print(" Declared by the icc and the world  "  +  cricketer.title() +"!")
    
# numerical lists

# range
for value in range(1,10):
    print(value)
    
#lists
numbers= list(range(1,50))
print(numbers) 

# evennumbers
even_number = list(range(2,11,2))
print(even_number)
 
# oddnumbers
odd_number = list(range(1,13,2))
print(odd_number) 

# squares
squares = []
for value in range(1,15):
    square = value ** 2
    squares.append(square)
print(squares)    

# cubes
cubes = []
for value in range(1,15):
    cube = value ** 3
    cubes.append(cube)
print(cubes) 

# comprehensions
squares = [value ** 2  for value in range(1,15)]
print(squares)

cubes = [value ** 3  for value in range(1,15)]
print(cubes)

# working with the part of the ;ist

# Slicing
players =['a', 'b', 'c', 'd', 'e']
print(players[0:1])
print(players[0:2])
print(players[0:3])
print(players[0:4])
# looping trough the slice
for player in players:
    print("the best player is ", player[0].title())
    
# copying
games = ['cod', 'cds', 'lotr', 'cds2']
friend_games = games[:]
print("my games RE")
print(games)

print("  \n my friends games are")
print(friend_games) 
