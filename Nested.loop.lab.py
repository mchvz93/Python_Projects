#get number f students and scores
num_students= int(input("how many students do you have?")) 
num_test_scores=int(input("how many test scores per student?"))

for student in range(num_students):
	total=0.0
	print("Student number", student+1)
	print("_ "*20)
	for test.num in range(num_test_scores):
		print("Test number ", test_num+1, end='')
		score=float(input(':'))
		total= total+score
	average=total/num_test_scores
	print('The average for student number', student+1, 'is', format (average,'.1f'))
	print()
