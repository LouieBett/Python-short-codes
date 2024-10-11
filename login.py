set_username = input("Pick your username: ")
set_password = input("Create your password: ")

add_firstname = input("Enter your first name: ")
add_surname = input("Enter your surname: ")

print("Username and password created!")

max_attempts = 3
attempts_left = max_attempts

while True:
    y_q = input("Do you want to login? Type Y to continue, type Q to quit: ")
    if y_q.lower() == 'y':
        enter_username = input("Enter your username: ")
        enter_password = input("Enter your password: ")

        if enter_username == set_username and enter_password == set_password:
            print("Login successful!")
            print("Welcome,",add_firstname, add_surname,"!")
            break
        else:
            attempts_left -= 1
            if attempts_left > 0:
                print(f"Incorrect username or password. You have {attempts_left} attempts left.")
            else:
                print("Maximum attempts reached. Account locked.")
                break
    elif y_q.lower() == 'q':
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please try again.")