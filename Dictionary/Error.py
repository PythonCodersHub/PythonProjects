# charlie = {1:'a', 2:'b', 3:'c', 4:'d', 5:'6'}
# print(charlie[10])

# handling error

charlie = {1:'a', 2:'b', 3:'c', 4:'d', 5:'6'}
if 500 in charlie:
    print(charlie[500])
else:
    print("notfound")    