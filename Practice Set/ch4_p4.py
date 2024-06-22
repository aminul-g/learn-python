n = 4
list = list(map(int, input("Enter the numbers: ").split()))
sum = 0
for i in range(n):
    sum += list[i]
    i += 1
print(sum)