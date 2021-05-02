alfa ={'color': 'green', 'code' : '7w'}
# print("the alfa  is", +alfa['color']+".")

alfa['color'] = 'black'
alfa['code']  =  '63w'
print("the alfa  is", alfa['color']+".")
print("the alfa  is", alfa['code']+".")
print(alfa)

alfa = {'x_position': 0, 'y-position' : 25, 'speed' : 'medium'}
print("original position" , +str(alfa['x_position']))
if alfa['speed'] == 'slow': 
    x_increment = 1
elif alfa['speed'== 'medium':
    x_increment = 2
else:
    x_increment = 3
    
alfa['x_position'] = alfa['x_position'] + x_increment       
print("New x-position: " + str(alfa['x_position']))

       