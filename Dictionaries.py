emp = {"Mohan":5000,"Madhu":6000,"Raghu":2500,"Priya":6000}
#fetching the salary of employee Priya
print(emp["Priya"])
Adding a new key value
If a key is not existing, then the below will add the key and the value
to the dictionary
emp["Shankar"] = 60000
print(emp)
#updating values for existing keys
emp["Raghu"] = 40000
print(emp)
#creating an empty dictionary
x = {}
x = dict()
#Extracting the keys and values from dictionary
print(list(emp.keys()))
print(list(emp.values()))
#iterating dictionaries, means iterating on keys
for elem in emp:
    print(elem, emp[elem])
Get me the name, salary, and bonous on salary which is 10% on the salary
math to compute final salary after applying bonus
salary = 5000
bonous = salary * (10/100)
print(bonous)
final_salary = salary + bonous
print(final_salary)
for elem in emp:
    print(elem,emp[elem],round(emp[elem]*1.1,2))
Get me the names of employees who earn more than 5000
Fetch the keys where the values are > 5000
for elem in emp:
    if emp[elem] > 5000:
        print(elem)
[elem for elem in emp if emp[elem] > 5000]
#Subsetting a dtict on non existiant key, results in an error
print(emp['Rama'])

check if the key is present, if so print the vlaue
else, print 'employee not found'

print(emp.get('Rama','Employee not found'))
print(emp.get('Raghu','Employee not found'))
print(emp.get('Rama'))

Dictionaries are mutable collection of heterogenous elements (called as values)which have named indexes.
dictionaries allows me to define indexes(called as keys), rather than using predefined indexes
keys cannot be duplicated, but values can be duplicate
emp1 = {"Mohan":5000,"Mohan":6000,"Raghu":2500,"Priya":6000}

print(emp1)
 Sorting dictionaries

Sorting on keys:
     1. Take the keys and convert to a list
     2. sort the list
     3. iterate the dictionary based on the sorted order of the list
emp_keys = list(emp.keys())
emp_keys.sort()
emp_keys
For every element in the sorted list of keys
fetch the key and the value from the dictionary
for elem in emp_keys:
    print(elem,emp[elem])
print(list(emp.items()))
##When a dictionary is converted to a list, then we get a list of tuples

new_dict = {'Name':'Gowrav','Age':24,'Country':'India'}

print(new_dict.keys())

# To Add new terms to the dictionary we use

new_dict['City']='Hyderabad'

print(new_dict)

punt = [1,2,3,4,5,6]

from functools import reduce
add_punt =[i for i in punt if i%2==0]
print(add_punt)