import time,sys
'''
begin = time.time()


new = tuple(range(10))
#print(new)
for i in new:
	print(i**2)

end = time.time()

print(end-begin)

ano = time.time()

lists = [i for i in range(11)]

print(lists)
for i in lists:
	print(i**2)
end_time = time.time()

#print(end_time-ano)

print(tuples)

print(id(tuples))

for i in tuples:
	print(i**2)


end = time.time()

print(end-begin)

new_time = time.time()

tuples = [1,2,4]

print(tuples)

print(id(tuples))

for i in tuples:
	print(i**2)



end_time = time.time()

print(end_time-new_time)

'''

lists= [i for i in range(1,11)]

tuples = tuple(range(1,11))

print(lists)
print(sys.getsizeof(lists))
print(tuples)
print(sys.getsizeof(tuples))



