name = input ("Please, enter your name! ")

print(f"Welcome to our quize game {name}")

score = 0

q1 = input("How many days are there in a week? ").lower()

if q1 == "seven":
    print("That's a correct answer! ")
    score += 1
else:
    print("Wrong answer! ")


q2 = input ("How many weeks are there in a month? ").lower()

if q2 == "four":
    print("That's a correct answer! ")
    score += 1
else:
    print("Wrong answer! ")

q3 = input("How to spell people? ").lower()

if q3 == "people":
    print("That's a correct answer! ")
    score += 1
else:
    print("Wrong answer! ")

print("That's the end of our quiz. Have a great day! ")

print(f" Your overall score is {score}.")

print(f"Your overall percentage is {(score*100)/3}")