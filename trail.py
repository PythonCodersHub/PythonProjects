# def foo(i):
#     return (((i*2)-3)%3)


# x = foo(6)
# print(x)

# here = "/home/httpd/html/test"
# print(here.split('/')[2])

# if (x == 1): 
#     print("joe")
# if (x=="1"): 
#     print("raja")
# if (x==4): 
#     print("raja")
# if (x==4): 
#     print("raja") 
# else: 
#     print("joe")
# if (x==4): 
#     print("raja") 
# elif: 
#     print("joe")
# if (x == 8): 
#     "joe"

# delim = "X"
# print(delim+"text"+delim+'delim'+"delim"+delim+str(93.2)+delim)

# def x():
#   def y ():
#     return "y"
#   return "x"
# print(y())

# if 1 < 3 < 3:
#     print(1); 
#     print(2); 
#     print(3)

# y = 12L
# z = 12
# v = y + z
# print(v)

# x = ['a', 'o', 'a', 'p', 'o', 'b']

# y = {i for i in x if i not in 'a'}

# print(no_dupe(x))

# x = [2, 2, 2]
# y = [4, 5, 6]
# zipped = zip(x, y)

# x_again, y_again = zip(*zipped)

# print(y_again)

# print(zipped-x)


# for i in range(0,5):
#   if i == 2:
#     continue
#   print(i)

# def text(sent):
#     return sent[::-1]

# print(text('new'))


# import pathlib
# def files(filename):
#     filename = pathlib.Path(filename)
#     if filename.exists():
#         lists = []
#         opening = open(filename,'r')
#         for line in opening:
#             lists.append(line.strip())
#         return lists
#     else:
#         print('No such thing exists')


# print(files('oops.txt'))


# else:
#     print('no')
# file1 = open('oops.txt','r')
# if file1
#     for line in file1:
#         print(line.strip())
 

# def show_me_money(values):
#     return round(values,3)
# print(show_me_money( 23.23400000001))

def strin(first,*second):
    new = []
    new.append(first)
    for i in second:
        new.append(i)
    new_list =sorted(new,key=len)
    return new_list
    
print(strin('a','bb','dddd','ccc'))



# Python code to sort a list by creating
# another list Use of sorted()
# def Sorting(lst):
# 	lst2 = sorted(lst, key=len)
# 	return lst2
	
# # Driver code
# lst = ["rohan", "amy", "sapna", "muhammad",
# 	"aakash", "raunak", "chinmoy"]
# print(Sorting(lst))
