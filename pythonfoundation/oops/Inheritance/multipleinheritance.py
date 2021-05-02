class Alfa:
    def delta(self):
        print("Alfa Method")
class Beta:
    def echo(self):
        print("Beta Method")
class Charlie(Alfa, Beta):
    print("Charlie Method")
foxtrot = Charlie()
foxtrot.echo()
foxtrot.delta()                   