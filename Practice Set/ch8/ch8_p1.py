def greatest(a,b,c):
    if b < a > c:
        return a
    elif a < b > c:
        return b
    else:
        return c
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
print("Greatest: ", greatest(a,b,c))