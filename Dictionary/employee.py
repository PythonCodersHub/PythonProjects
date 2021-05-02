a = {}

b = int(input("Enter the no of empoyee"))
c = 1
while c<=b:
    name = input("Enter the employee name")
    salary = input("Enter the salary")
    a[name] = salary
    c = c+1
    
for x in a:
    print("The name is ",x,"and salary is :",a[x] )      