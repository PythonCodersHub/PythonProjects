cars = ['ferrari', 'audi', 'benz', 'ford']
cars.sort()
print(cars)


for car in cars:
    if car == 'audi':
        print(car.upper())
    else:
        print(car.title())
        
bikes = ['yamaha','CBZ', 'Herohonda', 'Harleydavidson', 'Hellcat', 'R15']            
bikes.sort()
print(bikes)


for bike in bikes:
    if bike == 'Hellcat':
        print(bike.upper())
    else:
        print(bike.title())
            