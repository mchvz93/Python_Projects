#Get number of students and scores
NUM_STUDENTS = int(input("How many students do you have?: "))
NUM_TEST_SCORE = int(input("How many test scores per student?: "))

for students in range(NUM_STUDENTS):
    total = 0
    print("Student number", students + 1)
    print("_________________")
    for test_num in range(NUM_TEST_SCORE):
        print("Test number", test_num + 1, end= ' ')
        score = float(input(':'))
        total = total + score
        average = total / NUM_TEST_SCORE
        print('The average for student number',students + 1,'is', format(average\
              ,'.1f'))


'''Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
How many students do you have?: 3
How many test scores per student?: 3
Student number 1
_________________
Test number 1 :85
The average for student number 1 is 28.3
Test number 2 :96
The average for student number 1 is 60.3
Test number 3 :92
The average for student number 1 is 91.0
Student number 2
_________________
Test number 1 :56
The average for student number 2 is 18.7
Test number 2 :66
The average for student number 2 is 40.7
Test number 3 :77
The average for student number 2 is 66.3
Student number 3
_________________
Test number 1 :80
The average for student number 3 is 26.7
Test number 2 :60
The average for student number 3 is 46.7
Test number 3 :20
The average for student number 3 is 53.3
>>> 
>>> '''
