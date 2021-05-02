# Introduction
# dimensions = (200, 50)
# print(dimensions)
# Empty tuples
# alfa = ()
# print(alfa)
# print(type(alfa))

# tuples with group values
# emp_id =(12,20,40)
# std_id = 20, 40 , 60
# print(emp_id)
# print(type(emp_id))
# print(std_id)
# print(type(std_id))

# using the tuplefunction()
# a = [100,200,30,"Alfa"]
# b = tuple(a)
# print(b)
# print(type(b))

# a = tuple(range(1,10))
# print(a)
# print(type(a))

# Indexing
# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# b = tuple(range(1,12))
# print(b)
# print(b[0])
# print(b[1])
# print(b[2])
# print(b[3])
# print(b[4])
# print(b[5])
# print(b[6])
# print(b[7])
# print(b[8])
# print(b[9])
# print(b[10])
# print(b[-1])
# print(b[-2])
# print(b[-3])
# print(b[-4])
# print(b[-5])
# print(b[-6])
# print(b[-7])
# print(b[-8])
# print(b[-9])
# print(b[-10])
# print(b[-11])

# Slicing
# a = (10,20,30,40,50,60,70,80)
# print(a)
# print(a[0:5])
# print(a[0:7])
# print(a[1:7])
# print(a[2:5])

# looping trough the loops
# icecreams = ("Vanilla", "strawberry", "chocolate", "Nuts")
# for icecream in icecreams:
#     print(icecreams)
    
# icecreams = ("Vanilla", "strawberry", "chocolate", "Nuts")    
# for icecream in icecreams:
#     print(icecream.title() +", is the best title"+".")
#     print("my fav icecream is :  " +icecream.title()+"\n")
# print("the best ice cream is:", icecream.title() )    

# dimensions = (200,300)
# print(dimensions)
# for dimension in dimensions:
#     print(dimension)
# dimesions = (400, 600)
# print(dimensions)
# for dimension in dimesions:
#     print(dimension)
# sorting in tuple
# cars = ('ferrari', 'audi', 'benz', 'chevrolet', 'bmw', 'hyundai')
# print(cars)
# print(sorted(cars))
# print(len(cars))    

# cars = ('ferrari', 'audi', 'benz', 'chevrolet', 'bmw', 'hyundai')
# print(cars)
# cars.sort()    

# num = tuple(range(1,20))
# print(num)

# evennumber
# even_num = tuple(range(2, 20, 2))
# print(even_num)
# oddnumber
# odd_num = tuple(range(1, 24, 2))
# print(odd_num)
# squares
# squares =()
# for a in range(1,25):
#     square = a ** 2
#     # squares.append(square)
#     print(square)
     

# cubes = ()
# for b in range( 1, 25):
#     cube = b ** 3
#     print(cube)    

# players = ('CK', 'DB', 'LA','Tiger', 'Master', 'LM')
# print(players)
# print(players[0:5])
# print(players[0:4])

# b = (1,1,2,3,4,4,5,6,7,7,8,9,10,1,12,12,13,15)
# print(b.count(1))
# print(b.count(4))

# Tuple having the same objects
# emp_id = (1,2,3,4,5,6,7)
# print("The objects having the same ids:", emp_id)
# print(type(emp_id))

# parenthsis is optional for tuple
# emp_id = 1,2,3,4,5,67
# print(emp_id)
# print(type(emp_id))
# print(id)

# different elements  type

# names = (1,2,3,"dell")
# print(names)
# print(type(names))

# single value tuple
# name = ("dell " , )
# print(name)
# print(type(name))
# name=("Deltaforce")
# print(name)
# print(type(name))
# name=(11)
# print(name)
# print(type(name))

# concatenation
# a =1,2,3
# b =3,4,5
# c = a+b
# print(c) 

# Len
# b = (1,2,3,4,5,6,7,8,9)
# print(b)
# print(len(b))

# count
# a = 1,1,2,2,3,3,4,5,6,7,8,9,10,11,11,12,13
# print(a.count(1))
# print(a.count(2))
# print(a.count(3))
# print(a.count(11))

# index
# t = (10,20,30,40,50,60)
# print(t.index(10))
# sorted
# a = (65,20,3,30,50,60)
# b = sorted(a)
# print(a)
# print(b)
# reverse
# a = (65,20,3,30,50,60)
# b = sorted(a, reverse=True)
# print(a)
# print(b)
# min&max
# a = (65,20,3,30,50,60)
# print(min(a))
# print(max(a))

# packing tuple
a = 10
b = 20
c = 30
d = 40
t = a,b,c,d
print(t)

# unpacking tuple
t = (10,20,30,40)
a,b,c,d = t
print("a=",a,"b=",b,"c=",c,"d=",d) 