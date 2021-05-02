a = [100,200,300,400]
b = a
print(a)
print(b)
print(id(a))
print(id(b))

a[1] = 20
print(a)
print(b)
print(id(a))
print(id(b))
