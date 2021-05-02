def fact(sum):
    a = 1
    while sum>=1:
        a = a*sum
        sum = sum-1
    return a
for val in range(1,5):
        print("The factorial of",val,"is", fact(val))
        
def facto(num):
    b = 1
    while num >=1:
        b = b * num
        num = num-1
    return b
for i in range(1,12):
    print("the fact of num ber",i,"is:", fact(i))    
    

def f(add):
    c = 1
    while c>=1:
        c = c * add
        add =  add-1
    return c
for b in range(1, 25):
    print("the f valuse",b ,"is:", fact(b))        
