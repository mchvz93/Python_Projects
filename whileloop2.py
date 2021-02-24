#temperature check program
MAX_TEMP = 102.5
temp = float(input("Enter temperature: "))

while temp > MAX_TEMP:
    print("The temperature is too high")
    print("Turn on the air condition")
    temp = float(input("Enter temperature: "))

print("Temprature is cool now")
print("Clock again in 30 mins")


'''Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Enter temperature: 103
The temperature is too high
Turn on the air condition
Enter temperature: '''
