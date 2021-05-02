icecreams = ['Vanilla', 'Strawberry', 'Chocobar', 'fruitnut','rumraisins']
for icecream in icecreams:
    if icecream == 'rumraisins':
        print("Out Of Stock")
    else:    
        print("Adding" + icecream +".")
print("\n the ice cream is served")    


#EMptylist
icecreams = []
if icecreams:
    for icecream in icecreams:
        print("Adding" + icecream +".")
    print("\n ice cream is served")
else:
    print("Do you need any drink")        
    
    #Multiple lists
    icecreams =['Vanilla', 'Strawberry', 'Chocobar', 'fruitnut','rumraisins', 'Mango', 'Jelly']
    requested_icecreams = ['Blueberry','Mango', 'Jelly', 'vanilla', 'Strawberry', 'Chocobar', 'fruitnut','rumraisins']
    for requested_icecream in icecreams:
        if requested_icecream  in  icecreams:
            print("Adding" + requested_icecream + ".")
        else:
            print("We dont have the requested" + requested_icecream + ".")
    print("\n enter to exit")            
            
    