num = 3
if num<1:
    print("Less than 2")
elif num<2:
    print("Not a good idea")
else:
    print("Greater than 2")

for i in range(7):
    print(i,"squared is", i**2)

print("-"*100)

n = 5
while n > 0:
    print(n)
    n = n+1
    if n>30:
        break
print("-"*100)

n = 10
while True:
    print(n)
    n = n - 2
    if n == 0:
        break
print('Done!')

print("-"*100)
weights = [89,90,100,75,55,65,45,20]
count = 0
for elem in weights:
    #do the processing -> count
    count = count+1
print("No of elements in the list is : ", count)

print("-"*100)

numbers = [5,6,7,8,10]
squaredNumbers = []
for num in numbers:
    squaredNumbers.append(num**2) 
    #append add elements after the existing element
print(squaredNumbers)
for i in numbers:
    print(i)


b = 2
while 2<=b<=40:
    print(b)
    b+=2

for i in range(7):
    print("*",end=" ")

x = "Star Wars"
for i in x:
    print(i,end=" ")