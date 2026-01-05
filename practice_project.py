master_password = input("Enter the master password: ")

def view():
    with open("Archieve.txt", "r") as file:
        for line in file.readlines():
            print(line.rstrip())
 
def add():
    acc_number = input("Account number: ")
    name = input("Account name: ")
    password = input("Password: ")
    
    with open("Archieve.txt", "a") as file:
        file.write(f"Account number: {acc_number} | Name: {name} | Password: {password} \n")
        


while True:
    user_input = input("Would you like to view the existing password or add new ones (view/add) or type q to quit: ")

    if user_input == "q":
        break

    elif user_input == "view":
        view()

    elif user_input == "add":
        add()

    else:
        print("Invalid input! ")
        continue