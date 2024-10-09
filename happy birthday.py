import time

print("This is a python code to say happy birthday once you put your date of birth")

print("Press ANY key to continue")
input()

print("Enter needed information below")

#This asks for a user to enter the day they were born on
def get_day():
    while True:
        try:
            day = int(input("What day were you born (Number): "))
            return day #This makes it go back to the start of the def
        except ValueError: #This ignores the error
            print("Invalid input. Please enter a NUMBER.")
#This asks for a user to enter the month they were born in

def get_month():
    while True:
        try:
            month = int(input("What month were you born in? (Number) "))
            return month #This makes it go back to the start of the def
        except ValueError: #This ignores the error
            print("Invalid input. Please enter a NUMBER.")

#This asks for a user to enter the year they were born in
def get_year():
    while True:
        try:
            year = int(input("What year were you born in? "))
            return year #This makes it go back to the start of the def
        except ValueError: #This ignores the error
            print("Invalid input. Please enter a NUMBER.")

day = get_day()
month = get_month()
year = get_year()

print("Loading...")
time.sleep(3)

print("You were born in the worst year: ", day, "/", month, "/", year, "Your age is: ", 2024 - year,)