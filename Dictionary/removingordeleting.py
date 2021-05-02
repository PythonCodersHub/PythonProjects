# deleting dictionary
charlie = {1:'a', 2:'b', 3:'c', 4:'d', 5:'6'}
print("Old dict is", charlie)
del charlie[4]
print("After deleting the dictionary", charlie)

# del method
charlie = {1:'a', 2:'b', 3:'c', 4:'d', 5:'6'}
print("Old dict is", charlie)
del charlie[5]
print("After deleting the dictionary", charlie)

# clear method
charlie = {1:'a', 2:'b', 3:'c', 4:'d', 5:'6'}
print("before clearing dict is", charlie)
charlie.clear()
print("After clearing  dict is", charlie)

# Del method
charlie = {1:'a', 2:'b', 3:'c', 4:'d', 5:'6'}
print("before clearing dict is", charlie)
del charlie
print("After clearing  dict is", charlie)