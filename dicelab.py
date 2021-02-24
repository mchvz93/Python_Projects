#This program is the dice lab
#with random number

import random

dice1 = random.randint(1,6)
dice2 = random.randrange(6)+1

total = dice1 + dice2

print("You rolled a", dice1, " and a", dice2,"for a total of",total)


#>>> 
#You rolled a 3  and a 6 for a total of 9
#>>> 
