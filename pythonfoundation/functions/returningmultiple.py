#defining functions
def d(e,f,i,j):
    g = e + f
    h = e - f
    l = i * j
    k = i / j
    return g, h ,l,k
    #calling
x,y,z,a = d(30, 50,60,80)
print("the sum is", x)
print("the diff is", y)
print("the mul is", z)
print("the div is ", a)
   