n = 6
print("Enter the marks of students: ")
mark=list(map(int,input().split()))[:n]
mark.sort()
print(mark)