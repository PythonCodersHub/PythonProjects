import random
die1 = random.randint(1,6)
die2 = random.randrange(6) + 1

total = die1 + die2
print("you rolled", die1 ,"and the",
      die2, "for the total of", total )
input("\n enter to exit")