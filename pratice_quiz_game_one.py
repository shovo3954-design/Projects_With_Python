name = input("What is your name: ")
print("Welcome to our emperical quiz game! ")

age = input("Would you mind providing your name in order to give a appropiate questions set?")
print("Perfect!")

score = 0

q1 = input("What is the capital city of Bangladesh?: ").lower()

if q1 == "dhaka":
    print("That's a correct answer! ")
    score += 1

else:
    print("That's a wrong answer! ")

q2 = input("Who is the corrent leader of Bagladesh?: ").lower()

if q2 == "yunus":
    print("That's a correct answer! ")
    score += 1

else:
    print("That's a wrong answer! ")

q3 = input("Which one is the correct spelling? \na. Restaurant.\nb. Rastaurant.\nc. Resturent.\nd. Resteurent.  ").lower()

if q3 == "a":
    print("That's a correct answer! ")
    score += 1

else:
    print("That's wrong answer!")

print(f"Your overall score is {score} out of three.")
print(f"The overall percentance is {(score*100)/3} %. ")