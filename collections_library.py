from collections import Counter

print(help(Counter))

letters = Counter('ascnajvnmascvijvndsjasmasknjnijdnbfoksokacsancijndaijvn ')

# print(letters.most_common(3)) # returns the most common 3 elements

# print(sorted(letters)) # returns the unique elements in the counter

# print(letters['a']) # returns the count of a

del letters['a'] # deletes all the occurences of a from the counter letters

print(letters[a]) # To check whether the items are deleted or not

new = Counter('mynameiskhan')

letters.update(new) # For updating the previous counter

letters.clear() # To clear the contents in counter

print(letters)

scrap = Counter('ascsdnasAaaaascas')

print(scrap['a']) # To check the count of letter a in the counter

scrap['a']-=5 # Reduce a element in the counter by the required frequency

print(scrap['a'])









from collections import namedtuple

aviary = namedtuple('Bird',['Name','Wingtype','Speed'])

needle = aviary('Swift','Sharp',162)

print(needle.Wingtype)

# Python program to demonstrate
# ChainMap
	
	
from collections import ChainMap
	
	
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# Defining the chainmap
c = ChainMap(d1, d2, d3)
	
# print(c)

# print(type(c))