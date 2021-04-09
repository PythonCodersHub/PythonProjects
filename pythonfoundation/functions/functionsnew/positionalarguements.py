def sum(a, b):
    print (a+b)
sum(20, 30)

#Positional Arguements
def cars_set(cars_name, cars_type):
    print(f"The name of my car is{cars_name}")
    print(f"the  name of my car is {cars_name}, Model is {cars_type.title()}")

cars_set('ferrari 360', 'Sports')

def bikes_set(bikes_model, bikes_name):
    print(f"The bikes model is {bikes_model}")
    print(f"the name of the bike is {bikes_name} and model is {bikes_model}")
    print(f"the model of bike is {bikes_model} and name of bike is {bikes_name}")
bikes_set('Hell cat', 'Harley davidson')    

def jets_set(jets_model, jets_name, jet_model1, jet_name1):
    print(f"The name of the jet is {jets_name} , {jet_name1}")
    print(f"the model of jet is {jets_model} {jet_model1}")
jets_set('Fihgter', 'f-36', 'fighter' , 's-126')    