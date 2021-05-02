def player(first_name, last_name, age=''):
    name  ={'firstname': first_name, 'lastname':last_name}
    if age:
        name['age'] = age 
        return name
cricketer = player('Sachin', 'Tendulkar', age=24)    
print(cricketer)