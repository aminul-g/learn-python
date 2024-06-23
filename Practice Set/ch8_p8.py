def table(n):
    mul = 1
    i = 1
    while i <=10:
        mul = n * i
        print(f"{i} x {n} = {mul}")
        i+=1
n = int(input("Enter the number: "))
table(n)