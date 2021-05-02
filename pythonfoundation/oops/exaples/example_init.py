class Employee:
    def __init__(self):
        print("This is the constructor class")
emp = Employee()        

# explicit constructor
class Employee:
     def __init__(self):
         print('constructor')
emp = Employee()
emp.__init__()          