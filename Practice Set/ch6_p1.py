
''' Write a program to find the greatest of 
four numbers entered by the use'''
a = 10
b = 20
c = 40
d = 30
if b < a > c and a > d:
    print(f"{a} greatest")
elif a < b > c and b > d:
    print(f"{b} greatest")
elif a < c > b and c > d:
    print(f"{c} greatest")
else:
    print(f"{d} greatest")
