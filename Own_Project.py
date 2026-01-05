print("You are gladly wellcome to Our GK quiz!")

approval = input("Do you feel like joining our intelectual quiz game? ")

score = 0

if approval.lower() != "yes":
    quit()

ans_one = input("Which country imposed port curbs on Bangladeshi exports? ")

if ans_one.lower() == "india":
    print("You'ar absoletely correct!")
    score += 1
else:
    print("You are close. However, Your answer is not accurate")

ans_two = input("What was the 2024 student movement mainly about? ")

if ans_two.lower() == "protest":
    print("You'ar absoletely correct!")
    score += 1
else:
    print("You are close. However, Your answer is not accurate")


ans_three = input("Who gifted a controversial “Greater Bangladesh” map? ")

if ans_three.lower() == "yunus":
    print("You'ar absoletely correct!")
    score += 1
else:
    print("You are close. However, Your answer is not accurate")

ans_four = input("What is the percentage of girls married before 18 in Bangladesh? ")

if ans_four.lower() == "42":
    print("You'ar absoletely correct!")
    score += 1
else:
    print("You are close. However, Your answer is not accurate")

ans_five = input("What is the main cause of economic slowdown in 2025? ")

if ans_five.lower() == "politics":
    print("You'ar absoletely correct!")
    score += 1
else:
    print("You are close. However, Your answer is not accurate")


ans_six = input("Which neighbour is facing “strategic distancing” with Bangladesh? ")

if ans_six.lower() == "india":
    print("You'ar absoletely correct!")
    score += 1
else:
    print("You are close. However, Your answer is not accurate")

print(f"You got {score} out of 6")
print(f"Your overall percentage is {(score/6)*100}")