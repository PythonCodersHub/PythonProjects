class Bat:
    def a1(self):
        print("instance method")
b = Bat()
b.a1()
print(dir(Bat))        


class Call:
    def b1(self):
        print("instance method")
c = Call()
c.b1()
print(dir(Call))       


class Alfa:
    def beta(self):
        print("instance method")
charlie = Alfa()
charlie.beta()
print(dir(Alfa))         