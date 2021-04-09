# Debugging is the process of finding error in a set of computer instructions
'''
Examine Variables
Step forward line-by-lines
show code as it executes

CMD
h - help
w - where
s - steps(steps into function)
n -  execute next line
c - complete execution
l - list 3 lines before and after current line
s - step into function call
b - show list of all break points
b[int]    set break point at line number 
b[func]   break at function name
cl - clear all break points
cl[int]  clear break point at line number (c10)
p - print
'''


#import pdb
new = []
breakpoint()
for i in range(1,7):
    print(i,'Square is',i**2)
    new.append(i**2)


#pdb.set_trace()
print(new)


def sum(a,b):
    return a+b
x = 3
y = 4
print(sum(x,y))

import pdb

def my_func():
    x =5
    y =6
    print(x+y)
    return x+y

a = int(0.1)
b = 1.0
c = a+b

#breakpoint()

e = 0.1
f = 1.0
g = e +f


#breakpoint()

xy = my_func()

print('done')



pdb.set_trace()