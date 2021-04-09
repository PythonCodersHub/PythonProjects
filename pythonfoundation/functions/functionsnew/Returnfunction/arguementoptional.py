# def name(first_name, middle_name, last_name):
#     full_name = f"{first_name}, {middle_name}, {last_name}"
#     return full_name
# deltaforce = name("Brett", "Alfa", "Heart") 
# print(deltaforce)   


# def name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#         return full_name
# deltaforce = name("Bret",  "Hart")
# print(deltaforce)            

def total_cost(x, *y):
       sum=0
for i in y:
       sum+=i
   print(x + sum)

#calling function
total_cost(100, 200) #valid
total_cost(110, 226, 311) #valid
total_cost(11,) #valid
