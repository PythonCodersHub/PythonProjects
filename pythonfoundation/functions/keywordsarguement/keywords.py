def cars(model, cost):
    print(model,"the price is ", cost)
cars(model="benz", cost="3000000")
cars(model="Ford", cost="3000000")
cars(model="Ferrari", cost="3000000")


def employee(name, id, department):
    # print(name,"employee name is :", id, "employee id is :", department, "employee department is:")
    print(f"\n employee name is: {name.title()}, \n employee id is: {id.title()}, \n employee department is {department.title()}")
employee(name="Alfa", id="3600", department="Aerospace")

def details(id, name):
    print("THe emp id is:", id)
    print("The Employee Name is :", name)
details(id=2130, name="CKC")  
details(id=2148, name="Hell")  