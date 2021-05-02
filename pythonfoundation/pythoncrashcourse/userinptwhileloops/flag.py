prompt ="Enter the ball is headed to "
prompt+="\n press enter to quit the program"


active = True
while active:
    message = input(prompt)
    
if message == 'quit':
    active = False
else:
    print(message)        
         