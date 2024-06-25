'''Write a program to find out whether 
a student has passed or failed if it requires a 
total of 40% and at least 33% in each
subject to pass. Assume 3 subjects and 
take marks as an input from the use'''
n = 3
subject = {}
total_marks = 0
passed_all_subjects = True

for i in range(n):
    sub_mark = list(input("Enter your subject and marks: ").split())
    if len(sub_mark) == 2:
        sub, mark = sub_mark
        mark = int(mark)
        subject[sub] = mark
        total_marks += mark
        if mark < 33:
            passed_all_subjects = False

total_percentage = total_marks / n

if passed_all_subjects and total_percentage >= 40:
    print("Passed")
else:
    print("Failed")
