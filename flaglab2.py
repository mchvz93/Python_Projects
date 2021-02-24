#Find largest number till users enter a flag

num = int(input("Enter a value: "))
large = int(input("Enter a value: "))
while num != -999:
    if num > large:
        large = num
    num = int(input("Enter a value: "))
    print("The largest number is: ", large)


'''>>> 
Enter a value: 12
Enter a value: 64
Enter a value: 95
The largest number is:  64
Enter a value: 320
The largest number is:  95
Enter a value: 12
The largest number is:  320
Enter a value: 35
The largest number is:  320
Enter a value: -999
The largest number is:  320
>>>''' 
