from collections import Counter

# print(help(Counter))

letters = Counter('ascnajvnmascvijvndsjasmasknjnijdnbfoksokacsancijndaijvn ')

# print(letters.most_common(3)) # returns the most common 3 elements

# print(sorted(letters)) # returns the unique elements in the counter

# print(letters['a']) # returns the count of a

del letters['a'] # deletes all the occurences of a from the counter letters

#print(letters[a]) # To check whether the items are deleted or not

new = Counter('mynameiskhan')

letters.update(new) # For updating the previous counter

letters.clear() # To clear the contents in counter

scrap = Counter('ascsdnasAaaaascas')

# print('Count of a :',scrap['a']) # To check the count of letter a in the counter

scrap['a']-=5 # Reduce a element in the counter by the required frequency

#print("COunt of a after reducing its frequency",scrap['a'])


# print(Counter('abbb') & Counter('bcc')) # To check the common element and its frequency

# print(scrap) # To view the elements in the counter

#knuth example

c =  Counter({2:2,3:3,17:1})

product=1
for i in c.elements():
    product*=i
print(product)