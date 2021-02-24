#input

test1 = int(input("Enter test 1 score:")) 
test2 = int(input("Enter test 2 score:"))
test3 = int(input("Enter test 3 score:"))

#calculations
total = test1+test2+test3
avg= total/3

print("The average score is: ", avg)

if avg>=90 and avg<=100:
	print ('A')
if avg>=80 and avg<=89:
	print('B')
if avg>=70 and avg<=79:
	print('C')
if avg>=60 and avg<=69:
	print('F')
if avg<0 or avg>100:
	print("invalid")

""" """
