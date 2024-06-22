n = int(input("How many fruits you want to list:" ))
print("Enter the fruits name: ")
fruits=list(map(str,input().split()))[:n]
print(fruits)