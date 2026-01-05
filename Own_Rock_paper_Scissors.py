import random

computer_wins = 0
user_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or q to quit the game : ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_input = options[random_number]
    print(f"The computer system picked {computer_input}")

    if user_input == "rock" and computer_input == "scissors":
        print("You won the game")
        user_wins += 1


    elif user_input == "paper" and computer_input == "rock":
        print("You won the game")
        user_wins += 1

    elif user_input == "scissors" and computer_input == "paper":
        print("You won the game")
        user_wins += 1

    else:
        print("You lost the game")
        computer_wins += 1


print(f"Your final score is {user_wins}. And the final score of computer is {computer_wins} ")
print("Have a great day!")