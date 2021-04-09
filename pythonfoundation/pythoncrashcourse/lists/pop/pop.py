bikes = ['Honda', "CBR", 'KTM', 'Ninja']
print(bikes)

popped_bikes =  bikes.pop(2)
print(popped_bikes)

bikes = ['Honda', "CBR", 'KTM', 'Ninja']

last_owned = bikes.pop()
print(f" my last owned bike was  {last_owned.title()}")

#position popping from list

first_owned = bikes.pop()
print(f"THe first ownedbike was, {first_owned.title()}")

#remove item by value
bikes = ['Honda', "CBR", 'KTM', 'Ninja']
print(bikes)

bikes.remove('Ninja')
print(bikes)