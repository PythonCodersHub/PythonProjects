# dictionary function
# alfa = dict()
# print(alfa)
# print(type(alfa))

# dict tuple

# alfa= dict({1:'a', 2:'b', 3:'c', 4:'d', 5:'6'})
# print(alfa)
# print(type(alfa))

# alfa= dict([(1, 'a'), (2, 'b'), (3, 'c')])
# print(alfa)
# length
# alfa= dict({1:'a', 2:'b', 3:'c', 4:'d', 5:'6'})
# print(alfa)
# print(len(alfa))

# get
# alfa= dict({1:'a', 2:'b', 3:'c', 4:'d', 5:'6'})
# print(alfa)
# print(alfa.get(5))
# pop method
# alfa= {1:'a', 2:'b', 3:'c', 4:'d', 5:'6'}
# print(alfa)
# alfa.pop(1)
# print(alfa)

# popitem
alfa= {1:'a', 2:'b', 3:'c', 4:'d', 5:'6'}
print(alfa)
alfa.popitem()
print(alfa)

# Keysmethod
alfa= {1:'a', 2:'b', 3:'c', 4:'d', 5:'6'}
print(alfa)
for a in alfa.keys():
    print(a)
    
#Values mwthod
alfa= {1:'a', 2:'b', 3:'c', 4:'d', 5:'6'}
print(alfa)
for a in alfa.values():
    print(a) 
    
#items
alfa= {1:'a', 2:'b', 3:'c', 4:'d', 5:'6'}
for k,v in alfa.items():
    print(k,'------', v)
     