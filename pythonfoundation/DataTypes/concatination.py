x = ['a', 'b', 'c', 1, 20.10]
y = ['f']
print(x+y)

#repeation

print( x * 5 )
#slicing
print(x[:1])
print(x[1: -1])
#indexing
print(x[-1])
#appending
print(x.append('Hello'))
print(x)
#extend
x.extend(['aa', 'cc'])
print(x)
#insert
x.insert(1, 'QWelcome')
print(x)

print(x.pop(0))
print(x)