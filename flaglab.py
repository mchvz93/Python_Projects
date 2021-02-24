#while loop that demonstrates the use of flags

sum = 0
count = 0

#input
num = float(input("Enter a number, or -999 to quit: "))
while num != -999:
    sum = sum + num
    count = count + 1
    num = float(input("Enter a number, or -999 to quit: "))

    if count != 0:
        avg = sum/count
        print("The sum is: ",sum)
        print("The average is: ", avg)
    else:
        print("Division by zero")

'''Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Enter a number, or -999 to quit: 56
Enter a number, or -999 to quit: 82
The sum is:  56.0
The average is:  56.0
Enter a number, or -999 to quit: 89
The sum is:  138.0
The average is:  69.0
Enter a number, or -999 to quit: 82
The sum is:  227.0
The average is:  75.66666666666667
Enter a number, or -999 to quit: 96
The sum is:  309.0
The average is:  77.25
Enter a number, or -999 to quit: -999
The sum is:  405.0
The average is:  81.0
>>> '''
