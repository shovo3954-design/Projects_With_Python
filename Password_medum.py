import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    player = input("Enter the number of player between 2 and 4.: ")

    if player.isdigit():
        player = int(player)

        if 2 <= player <= 4:
            print("You choose the correct number. Best of luck for the forthcomming game.")
            break
        else:    
          print("Player must be from 2 to 4")
    else:
            print("Invalid Number")

max_score = 100
player_score = [0 for _ in range (player)]

while max(player_score) < max_score:

    for i in 
    should_roll = input("Would you like to roll (y)? ").lower()
    current_score = 0

    if should_roll != "y":
        break
    else:
        value = roll()
        if value == 1:
            print("Your rolled a 1. Turn done!")
        else:
            current_score += value
            print(f"You rolled a: {value}")