start_num = int(input("Enter the starting number: "))
ending_num = int(input("Enter the ending number: "))
product = 1
for i in range(start_num, ending_num+1):
    product *= i
    i+=1
print(f"The factorial of {ending_num} is {product}")