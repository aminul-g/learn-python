from random import choice


computer = choice([-1, 0, 1])

you = input("Enter a character from s, w and g: ")

your_str = {
    "s": -1,
    "w": 0,
    "g": 1,
}

revers_str = {
    -1: "Snake",
    0: "Water",
    1: "Gun",
}

if you not in your_str:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    you_int = your_str[you]
    print(f"You chose {revers_str[you_int]} \nComputer chose {revers_str[computer]}")

    if computer == you_int:
        print("It's a draw")
    elif (computer == -1 and you_int == 1) or (computer == 0 and you_int == -1) or (computer == 1 and you_int == 0):
        print("You Win!")
    else:
        print("You Lose!")
