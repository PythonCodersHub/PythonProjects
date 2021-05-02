# Introduction

# dress ={'color':'green' , 'code': '33'}
# print(dress['color'])
# print(dress['code'])

# empty dictionary
# name ={}
# name[1]="dict"
# name[2]="hello"
# name[3]="well"
# print(name)

# accessing dictionary using keys

# name={1:'dict', 2:'hello', 3: 'well'}
# print(name[1])
# print(name[2])
# print(name[3])

# key error 
# name={1:'dict', 2:'hello', 3: 'well'}
# print(name[30])

# Handling error
# name={1:'dict', 2:'hello', 3: 'well'}
# if 400 in name:
#     print(name[400])
# else:
#     print('key not found')    

# empinfo
# emp  ={}
# n =int(input("Enter the employee number"))
# i  = 1
# while i<=n:
#     name = input("Enter the  employee name")
#     salary=input("Enter the salary") 
#     emp[name] = salary
#     i = i+1
    
# for x in emp:
#     print("The name of employee is:", x, "salary is", emp[x])      
           

# score = {}
# runs = int(input("Enter the runs made by the batsman"))
# a = 1
# while a<=runs:
#     name = input("Enter batsman name")
#     centuries = input("Enter the centuries")
#     score[name] = centuries
#     a = a+1
# for x in score:
#     print("THe runs made by batsman",x,"centuries are", score[x])
        
# Updating dictionaries
# a ={'1':'All', '2':'dell', '3':'mill'}
# print(a) 
# a[4] = 'will'
# print(a)

# case2
# a ={1:'All', 2:'dell', 3:'mill'}
# print(a)
# a[3] = 'delta'
# print(a)

# Deleting from dictionary

# a ={'1':'All', '2':'dell', '3':'mill'}
# print(a)
# del a['1']
# print(a)

# clear

# a ={'1':'All', '2':'dell', '3':'mill'}
# print(a)
# a.clear()
# print(a)

# dict function
# a = dict()
# print(a)
# print(type(a))

# length function
# a ={'1':'All', '2':'dell', '3':'mill'}
# print(a)
# print(len(a))

# get function
# a ={1:'All', 2:'dell', '3':'mill'}
# print(a.get(1))
# print(a.get(3))

# pop
a ={1:'All', 2:'dell', '3':'mill'}
a.pop(key, 1)