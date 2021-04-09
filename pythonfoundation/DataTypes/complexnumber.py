#Complex number ceation

z = complex(6, 9)
print(z)

y = complex(6, -3)
print(y)


a = 6+4j
b = 3+5j
c = a+b
print(c)

print(type(c))

#print real and imaginary part
a = 4+9j
#real
print(a.real)
#imaginary
print(a.imag)
a = 6+3j
#Real
print("The complex number : Real Nmber is =", a. real)
#ImaginaryPart
print("The complex number : Imaginary Number is=", a. imag)
#Conjugate
print("The complex number is : Conjugate Number is=", a. conjugate())

#Operations

c1 = 6+3j
c2 = 4+6j

#Additon
print("The result is  :", c1+c2)
#Sub
print("The result is  :", c1-c2)
#Multiplication
print("The result is  :", c1 * c2)
#Division
print("The result is  :", c1 / c2)
# print("The result is  :", c1 % c2)
# print("The result is  :", c1 // c2)

