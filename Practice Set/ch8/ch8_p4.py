def sum(n):
    s = 0
    if n ==1:
        return 1
    else:
        return sum(n-1) +n 
n = int(input("Enter a number: "))
print(sum(n))