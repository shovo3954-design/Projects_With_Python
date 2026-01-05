master_password = input("Enter the master password: ")

def view():
    with open("own_password.txt", "r") as file:
        for line in file.readlines():
            print(line.rstrip())


def add():
    name = input("Account Name: ")
    password = input("Password: ")

    with open("own_password.txt", "a") as file:
        file.write(f"Account Name: {name}, Password: {password}, \n")

        
        

while True:
    user_input = input("Would you like to add password or view the existing ones (add or view)? and if you want to quit, write q.: ").lower()

    if user_input == "q":
        break
    elif user_input == "view":
        view()

    elif user_input == "add":
        add()
    else:
        print("Invalid Input")
        continue
