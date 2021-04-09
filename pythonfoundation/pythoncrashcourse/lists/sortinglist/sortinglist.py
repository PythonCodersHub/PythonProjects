#sorting list permanently

cars = ['Ferrari', 'Benz', 'Audi', 'Elantra', 'Swift']
print(cars)
cars.sort()
print(cars)
print("\n length")
#length 
print(len(cars))

#Reverse Sorting
print("\n Reverse")

cars = ['Ferrari', 'Benz', 'Audi', 'Elantra', 'Swift']
print(cars)
cars.sort(reverse=True)
print(cars)

print("\n Sorted")
#Sorting list temporarily with sorted
print("The original list")
print(cars)
print("The second list is")
print(sorted(cars))
print("\n ReverseOrder")
#REverseorder
cars = ['Ferrari', 'Benz', 'Audi', 'Elantra', 'Swift']
print(cars)
cars.reverse()
print(cars)