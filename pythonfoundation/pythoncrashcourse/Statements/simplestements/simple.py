cars = ['ferrari', 'audi', 'benz', 'ford']
print(cars)
cars.sort()

for car in cars:
    if car == 'audi':
        print(car.upper())
    else:
        print(car.title())    