def name(first_name,last_name):
    full_name = first_name + '  ' + last_name
    return full_name.title()
while True:
    print("Enter your name")
    print("Enter 'q' to quit")
    
    first_name = input("Enter your first name")
    if first_name == 'q':
        break
    
    last_name = input("Enter your last name")
    if last_name == 'q':
        break
    
person = name(first_name, last_name)     
print(person)  