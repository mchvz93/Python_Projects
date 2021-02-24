#Guessing game that demonstrates import random method

import random

print("Guess my number between 1 to 100")

#set initial values
my_numbers = random.randint(1,100)
guess = int(input("Take a guess..."))
tries = 1

while guess != my_numbers:
    if guess > my_numbers:
        print("Lower...")
    else:
        print("Higher...")

    guess = int(input("Take a guess..."))
    tries = tries + 1

print("You guess it right! The number is: ",my_numbers)
print("You took", tries,"tries!\n")



'''Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Guess my number between 1 to 100
Take a guess...56
Higher...
Take a guess...69
Higher...
Take a guess...79
Higher...
Take a guess...89
Lower...
Take a guess...85
Lower...
Take a guess...86
Lower...
Take a guess...82
Lower...
Take a guess...80
Higher...
Take a guess...81
You guess it right! The number is:  81
You took 9 tries!

>>> '''
