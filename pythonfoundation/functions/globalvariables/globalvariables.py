a = 10
b = 0

def charlie():
    print("function of charlie is charlie() :", a)
    print("function of echo is charlie()", b)
def foxtrot():
    print("function of Hotel is foxtrot():", a)
    print("finction of  juliet is  foxtrot():", a)

charlie()
foxtrot()

a ="romeo"
b="dela"
c="Kombat"
d="EInsh"
def echo():
    print("the function of echo is echo()", a)
    print("the function of echo us echo()", b)
def golf():
    print("the function of echo is golf()", c)
    print("the function of echo us golf()", d)
echo()    
golf()

x ="global"
def well():
    print(x)
well()    

# b = "global"
# def mul():
#     b = b * 4
#     print(x)
# mul()    

#Using both global and local variable

#global variable

a = "global"
def hawk():
    global a
    b = "Deltaforce"
    a =  a * 4
    print(a)
    print(b)
hawk()  

#Global and local having same name

a = 30
def sum():
    a = 50
    print("the sum of c is", a)
def s():
    print("the sum of c is",  a)
sum()
s()        
    
a = 30
def d():
    global a
    a = 80
    print("the ans is :", a)
def e():
    print("the ans is", a)
d()
e()


s = 1
def b():
    s = 2
    print(s)
    print(globals()["s"])
b()    