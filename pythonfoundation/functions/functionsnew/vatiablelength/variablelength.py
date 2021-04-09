# def total_cost(x , *y):
#     sum = 0
#     for i in y:
#         sum+= 1
#         print(x + sum)
# #calling function
# total_cost(100000, 300000)
# total_cost(30000, 500000, 1200000)
# total_cost(11,)        

def total_price(x , *y):
    sum = 0
    for i in y:
        sum+= 1
        print(x + sum)

total_price(300000, 600000)
total_price(100000, 600000, 900000)
total_price(11,)