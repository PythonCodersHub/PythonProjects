#search
aeroplane = [737, 747, 777, 787]
search = int(input("enter the series number: "))
for element in aeroplane:
    if search == element:
        print("Aeroplane series is  found :")
        break
else:
    print("series does not match")
     