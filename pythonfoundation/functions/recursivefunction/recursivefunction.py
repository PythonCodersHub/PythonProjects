def factorial(a):
    if a == 0:
        return 1
    else:
        return (a * factorial(a-1))


num = 8
print("the factorial of ", num, "is", factorial(num))


def fact(b):
    if b == 1:
        return 1
    else:
        return(b * fact(b-1))


print("the fact is",  fact(6))


def fact(c):
    if c == 2:
        return 2
    else:
        return (c * fact(c-1))


print("the fact is", fact(7))


def fact(d):
    if d == 3:
        return 3
    else:
        return (d * fact(d-1))
print("the fact is", fact(8))            
