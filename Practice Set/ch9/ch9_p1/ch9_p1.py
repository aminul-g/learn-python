'''
Write a program to read the text from a given file ‘poems.txt’ and find out 
whether it contains the word ‘twinkle’.
'''
with open("poems.txt", "r") as f:
    text = f.read() 

if "twinkle" in text.lower(): 
    print("The word is present")
else:
    print("The word is not present")
