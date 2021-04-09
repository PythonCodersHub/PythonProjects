# def scores():
#     runs= 18563
#     print(runs)
# scores()    

# def scores():
#     runs = 20689
#     print(runs)
# def scores_1():
#     print(runs)
# scores()
# scores_1()

def axe():
    y = "chopping"
    print(y)
axe()    

#Global and local having same name

a = 30
def sum():
    a = 50
    print("the sum of c is", a)
def s():
    print("the sum of c is",  a)
sum()
s()      

s = 1
def b():
    s = 2
    print(s)
    print(globals()["s"])
b()    