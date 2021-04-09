# def hello(name, msg):
#     print("Hello", name + ',' + msg)
# hello('Delta',  'Welcome')

# Using the default arguements

def welcome(name, code="Welcome to python"):
    print("Hello", name + ', ' + code)


welcome('delta')
welcome('bruce')

# def greet(msg="Welcome to coding", name):
#     print("Welcome", name + ', ' +  msg)
# greet('delta',  msg)

# keyword arguments

def Hola(name = 'deltaforce', salary='3000'):
    print("Welcome to", name+ ', ' + salary)
Hola('deltaforce', '3000')     


# def Hola(name ='deltaforce', msg='Welcome to python'):
#     print("Hello", name + ', ' + msg )
# hola('deltaforce', msg)


# Arbitrary Arguements

def cricket(*batsmen):
    for batsmen in batsmen:
        print("the best batsmen is :", batsmen)


cricket('col ck', 'Don bradman', 'Sunil Gavaskar',
        'Kapil dev', 'SachinTendulkar')
