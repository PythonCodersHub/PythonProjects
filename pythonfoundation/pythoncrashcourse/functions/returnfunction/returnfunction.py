# def name(first_name, last_name):
#     full_name = first_name +'  '+ last_name
#     return full_name.title()
# cricketer = name('charlie', 'bets')
# print(cricketer)


# def game(first_name, last_name):
#     total_game = first_name + last_name
#     return total_game.title()
# deltaforce = game('cds' , 'dbc')
# print(deltaforce)


# optional arguments
# def name(first_name, middle_name, last_name):
#     full_name = first_name+' '+middle_name+''+last_name
#     return full_name.title()
# batsman = name('sachin', 'ramesh', 'tendulkar')    
# print(batsman)

# optional arguments
# optional arguement
def full_name(first_name,middle_name,last_name):
    full_name = first_name+ ' ' +middle_name+ ' ' +last_name
    
    return full_name.title()
cricketer = full_name('Sachin', 'Ramesh', 'Tendulkar')
print(cricketer)

def full_name(first_name, last_name, middle_name=''):
    if middle_name:
        f_name = first_name+ '  ' + middle_name + '  ' + last_name
    else:
        f_name = first_name+'  '+ last_name
        return f_name.title()
    
cricketer = full_name('Sachin','Tendulkar')
print(cricketer)
cricketer = full_name('Sachin', 'Ramesh', 'Tendulkar')
print(cricketer)        

