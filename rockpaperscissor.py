name = input("Please enter your name?: ")

print(f"Welcome our game {name}")

import random
computer_wins = 0
user_wins = 0
options = ["rock", "paper", "scissors"]

while True:

    user_input = input ("If you want to play, then write p or type q to quit. : ").lower()

    if user_input == "q":
        break
    elif user_input == "p":
        print(f"Let's continue {name}")

    user = input("Typer Rock/Paper/Scissors: ")

    if user not in options:
        continue



    random_number = random.randint(0, 2) #rock  = 0, paper = 1, scissors = 2
    computer_input = options[random_number]

    print(f"Computer picked {computer_input}")



    if user == "rock" and computer_input == "scissors":
        print (f"You won the game {name}")
        user_wins += 1

    elif user == "paper" and computer_input == "rock":
        print (f"You won the game {name}")
        user_wins += 1

    elif user == "scissors" and computer_input == "paper":
        print (f"You won the game {name}")
        user_wins += 1

    else:
        print(f"You lost the game {name}")
        computer_wins += 1


print(f"Your overall score is {user_wins} and computer won {computer_wins}")