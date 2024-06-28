from random import *
randomNum = randint(1, 100)
num = -1
guesses = 0
while (num != randomNum):

   num = int(input("guess the  number: "))
   if(num > randomNum):
      print("Lower number please: ")
      guesses += 1
   elif(num < randomNum):
      print("! Higher number please !")
      guesses += 1
print(f"You have guesses the number {num} correctly in {guesses} attempt\n")
   
      