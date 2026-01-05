name = input("Would you mind giving your name?: ")
print(f"Welcome {name} to our advanture game. ")

ans = input("The road you are heading to is about to end. You have two options. Which way will you go right or left" ).lower()

if ans == "left":
    ans2 = input("You have come in fornt of a river. Now, you can walk aroud or swim. If you want to walk, write walk or if you feel like swim, write swim. ")
    if ans2 == "swim":
        print("I wil undoubtly die because of the alligator and the anaconda")

    elif ans2 == "walk":
        print("You will ran out of water and die")

    else:
        print("Not a valid option. You lost!")

elif ans == "right":
    print()
    

else:
    print("Not a valid option. You lost!")
