#Range
for value in range(1, 5):
    print(value)

for value in range(1, 6):
    print(value)

for value in range (10,30):
    print(value)    

print("\n Lisitng numbers ")
#Lisiting numbers using range

numbers = list(range(20,40))    
print(numbers)

print("\n EvenNumbers")
#Even numbers
evennumbers= list(range(2, 20, 2))
print(evennumbers)

print("\n odd numbers")
oddnumber =list(range(1, 21, 2))
print(oddnumber)

print("\n squares")

squares = []
for value in range(1, 10):
    square = value ** 2
    squares.append(square)
print(squares)    

#Statistics

digits = [1,2,3,4,5,6,7,8,9,10]
print(min(digits))
print(max(digits))
print(sum(digits))