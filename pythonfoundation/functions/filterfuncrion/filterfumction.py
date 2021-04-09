product_cost = [1000000, 50000000, 8000000, 12500000]
gta_car_price = filter(lambda x: x>8000 , product_cost)
a = list(gta_car_price)
print("The hottest car is", a)