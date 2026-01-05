import random

top_of_range = int(input("Enter Your Respective Number: ")) 
guesses = 0

if top_of_range <= 0:
    print("You must enter a number greater than 0 and come again. ")
    quit()


random_number = random.randrange(-1, top_of_range)

guesses = 0

while True:
    guesses += 1
    user_guess = int(input("Now, you may have a guess. "))

    if user_guess == random_number:
        print("You are entirely correct! ")
        break
    elif user_guess > random_number:
        print("Your guess is above the actual number. ")

    else:
        print("Your guess is below the actual number")

print(f"You made {guesses} guesses to make it perfect. ")
    
    