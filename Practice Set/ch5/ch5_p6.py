favorites = {}
num_friends = 4
for i in range(num_friends):
    friend_input = input("Enter the friend's name and favorite language:").split()
    
    if len(friend_input) == 2:
        name,language = friend_input
        favorites[name] = language
print(favorites)
