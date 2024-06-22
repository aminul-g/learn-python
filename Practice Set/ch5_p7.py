favorites = {}
num_friends = 4
for i in range(num_friends):
    friend_input = input("Enter the friend's name and favorite language:").split()
    
    if len(friend_input) == 2:
        name,language = friend_input
        favorites[name] = language
print(favorites)

'''
    If the names of 2 friends are same; what will happen to the program in problem 
    6?
    It will take the last value of the key
'''