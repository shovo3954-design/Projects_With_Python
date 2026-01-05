print("Wellcome to our computer quiz!")

playing = input("Do you feel like playing the game? ")

score = 0

if playing.lower() != "yes":
    quit()

print("Let's jump into our game. ")

question_one = input("What does CPU means? ")
if question_one.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("You'ar too close. However, the answer is not accurate. ")

question_two = input("What does GPU stand for? ")
if question_two.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("You'ar too close. However, the answer is not accurate. ")

question_three = input("What does RAM stand for? ")
if question_three.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("You'ar too close. However, the answer is not accurate. ")

question_four = input("What does PSU stand for? ")
if question_four.lower() == "power suply":
    print("Correct!")
    score += 1
else:
    print("You'ar too close. However, the answer is not accurate. ")

print(f"Your overall score is : {score} out of 4")
print(f"You got {(score/4)*100}%")


