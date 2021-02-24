#Marco Chavez
#Student ID 913519
#CS 10
#HW2PS1

import random

guess=0
lottnum = random.randint(10,99) 

#input
print("Lottery Game")
guess = int(input("Enter a two digit number: "))

#calc
lottones= lottnum//10
lotttens= lottnum%10

guessones= guess//10
guesstens= guess%10

#output

if lottnum==guess:
	print("Your numbers are an exact match, you won $10,000")
elif lottones==guesstens and lotttens==guessones:
	print("Your numbers are almost a match, wrong order, you won $3,000")
elif (lottones==guesstens or lottones==guessones or lotttens==guessones or lotttens==guesstens):
	print("At least one of your numbers match, you won $1,000")
else:
        print("You LOST LOSER!!!!!!!! YOU WIN NOTHING!!!!!!!!")
print ("Winning number was: ", lottnum)

'''Lottery Game
Enter a two digit number: 95
At least one of your numbers match, you won $1,000
Winning number was:  99'''
