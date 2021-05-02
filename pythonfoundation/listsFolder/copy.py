x = ['a', 'b', 'c']
y = x.copy()
print(x)
print(y)
print(id(x))
print(id(y))

mybikes = ['cbz', 'ninja', 'harley', 'Enfield', 'tomcat']
friendbikes = mybikes[:]
print(mybikes)
print("\n",friendbikes)