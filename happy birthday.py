import time

print("This is a python code to say happy birthday once you put your date of birth")

print("Press ANY key to continue")
input()

print("Enter needed information below")

def day_back():
    try:
        day = int(input("What day were you born (Number): "))
    except ValueError:
        print("Invalid input. Please enter a NUMBER.")
        balls()
def month_back():
    try:
        month = int(input("What month were you born in?(Number) "))
    except ValueError:
        print("Invalid input. Please enter a NUMBER.")
def year_back():
    try:
        year = int(input("What year were you born in? "))

    except ValueError:
        print("Invalid input. Please enter a NUMBER.")

print("Loading...")
time.sleep(3)

print("You were born on: ",day,"/",month,"/",year,"Your age is: ",2024-year)