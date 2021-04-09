# Tuples are immutable

tup = (1,2,3)

print(tup)

print(type(tup))

#print(dir(tuple))

tuple2 = (1,2,3,"Gowrav",'Bobby',[1,2,3],{'a':1,'b':2})

print(tuple2[6].keys())


#tuple[1] = 'Bob' # This throws an error as item assignment is not possible

# parenthesis are optional in creating tuples

conti = 1,2,3,4,5,6,7,7

print(conti[0])

# Everytime the variable is assigned with new value,it allocates new memory
t= (1,2,3)
print(id(t))

t = (1,2,3,4)
print(id(t))

some = [1,2,3,1,4,5,6,1,1]

ind  = [ i for i in some if some[i]==i]

print(ind)

