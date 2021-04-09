def name(first_name, last_name):
    full_name = f"{first_name}, {last_name}"
    return full_name.title()
employee = name("jack", "kallis")
print(employee)    


def course(course1, course2):
     courses = f"{course1}, {course2}"
     return courses.title() 
codingcourses = course("Python", "Java")
print(codingcourses)        


def cars(model, cost):
    car = f"{model} , {cost}"
    return car.title() 
Amazing = cars("Ferrarri", 3650000)
print(Amazing)    

def jets(Model, types):
    jet = f"{Model}, {types}"
    return jet.title()
defence = jets('F16', 'Fighter')
print(defence)  
print(type(jets))


def tickets(normal , vip):
    ticket = f"the price is {normal}, the price is{vip}"
    return ticket.title()
Dones = tickets(normal="150", vip="300") 
print(Dones)   

def value(num):
    if num>=0:
        return num
    else:
        return -num
print(value(2))   
print(value(-4))         
