#input
test1 = int(input("Enter test 1 score:")) 
test2 = int(input("Enter test 2 score:"))
test3 = int(input("Enter test 3 score:"))

#calculations
total = test1+test2+test3
avg= total/3

print("The average score is: ", avg)

if avg>=90:
	print('A')
if avg>=80:
	print('B')
if avg>=70:
	print('C')
if avg>=69:
	print('F')

