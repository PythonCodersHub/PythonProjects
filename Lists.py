'''old = ['Something','Will','Be' ,'Good','TOday']

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


Conclusion :  x and z will contain the same data, will refer to the different locations in memory.
z = x.copy(), will result in deep copy of the elements of x into z, which means that all the elemnts in x will be copied to a different location in memory
x and z are 2 independent copies
any changes to x will not reflect in z and vice versa

# # list menthods
# 1. list()
# 2. append()
# 3. extend()
# 4. index()
# 5. copy()
# 6. remove()
# 7. pop()
# 8. reverse()
# 9. sort()

a=[1,2,3]
b=[4,5,6]

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
x.reverse()

print(x)

x.sort()

print(x)

x.reverse()

x.insert(4,3)

print(x)
# A combination of sort and revrse, will result in the list in descending order

len(x) # find the length of any collection

y = [100,200,2,2,3,55,6,8,8,9,10,-50]

len(set(y))

len(y)

#set method removes duplicate elements from the list 
# and it also  sorts the list in increasing order
sety = set(y)
print(sety)

help(x)

#distinct count of the elements of the list
len(set(y))

# Equivalent and identical lists are those created with shallow copy
# After your deep copy(using .copy()), the two lists are equivalent and not identical


#help(x) - details about all the methods of object x


#dir(x) - lists all the methods of object x

#How many times 8 occours in the list
print(y.count(8))'''

# 05/04/2021
# Accessing elements in the list
basket = ['Eggs','Chicken','Mutton','Fish','Chips']

print(basket[0])


# Accessing elements using Loops

# Using For Loop
random = [0,1,2,3,4,5,6,7,8]
print(random[:5]) # print(variable[inclusive index : exclusive index])

# Using While Loop
a = [1,2,3,4]
i =0
while(i<len(a)):
    print(a[i])
    i+=1

# Finding the length of the list

print(len(random))

# Finding the count in the list

recursive = [1,2,1,2,3,1,3,4]

print(recursive.count(1))

# Appending the elements to list

basket = ['Eggs','Chicken','Mutton','Fish','Chips']

basket.append('Milk')

print(basket)

blend = [1,2,3,'One','Two']

print(blend.append('Three'))

# Inserting elements to a list, adds elements to the index 
# and the previous element is increased by one index

pop = ['Corona','Is','Every','Where']

pop.insert(1,'Virus')

print(pop)

# Append adds elements elements to the last
# By using insert, elements can be added at any index

# Reverse method

rand  = [1,7,3,32,34,64,12,2]

rand.reverse()

print(rand)

# Sorting, to work all the elements should be homogeneous

some = [12,3,21,45,1,34,4]

some.sort()
print(some)


# Aliasing

first_list = [1,2,3,4,5]

copy_list = first_list

first_list[0] = 'One'

print(first_list) # Displaying the original list

print(copy_list) # Displaying the copied list

print(id(first_list))

print(id(copy_list))

# Cloning , it creates different memory locations

first = [1,2,3,4,5,6]

second = first[:]
second[2] = 'First'
first[2] = 'Second'

print(first)
print(second)

# Copy method

tran = first.copy()

print(id(first))
print(id(tran))


# Multiply Operator
print(first*2)

# List comprehension

first = [i*2 for i in range(1,11)]

print(first)

s = [i for i in range(1,21) if i%2==0 ]

print(s)


new_trial = [i if i%2==0 else i*100 for i in range(1,11)]
print(new_trial)

print('Done')