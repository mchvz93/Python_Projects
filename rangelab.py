#program list number and it's square
#uses the in range method

start = int(input("Enter start numbers: "))
end = int(input("Enter end numbers: "))

print()
print('Number \+ Square')
print('---------')

for num in range(start,end):
    square = num ** 2
    print(num, '\t', square)


'''Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Enter start numbers: 5
Enter end numbers: 8

Number \+ Square
---------
5 	 25
6 	 36
7 	 49
>>> ''
