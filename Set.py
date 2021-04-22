# new_set = [1,1,2,3,4,5,5,6] # List with duplicate elements

# print(new_set)

# # To delete the duplicates we can use
# print(set(new_set))

# print('Type of the Data structure is ',type(new_set))

# # While using step values use inclusive, exclusive and stride
# range_set = {i for i in range(0,10,2)}

# print(range_set)

# print('Type of the Data structure is ',type(range_set))

#Creating a empty set

empty_set = set()

# print(empty_set)

# Methods in set
# print(dir(set))

# Adding new elements to the set
#Only one element can be added to the set
# empty_set.add('Jango')

# print(empty_set)

# list_items = ['A','B','C','D']

# empty_set.update(list_items)

# print('After adding the new elements ',empty_set)

# additional_set = {'Marco','Polo'}

# another_set = ["Jango","Fett"]
# empty_set.update(additional_set,another_set)

# print('After adding new elements from another set ',empty_set)

# Using intersection

# wars = {'Star','Wars','Light'}

# trek = {'Star','Trek'}

# # print(wars.intersection(trek))

# # Using copy

# s={1,2,3,45}

# print(id(s))
# s1=s.copy()
# print(id(s1))

# s.add(40)
# print(s)
# print(s1)

# print((dir(set)))


# wars = {'Star','Wars','Light'}

# trek = {'Star','Trek'}

# print(wars.symmetric_difference(trek))

# print(help(set.symmetric_difference))

from copy import *


new_list = [1,2,[3,4,5],6]
shallow_copy  = copy(new_list)

deep_copy = deepcopy(new_list)


new_list[2][2] = 50

print(new_list)

print(shallow_copy)

print(deep_copy)

print('Done!')