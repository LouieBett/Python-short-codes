import time

print("This is a python code to say happy birthday once you put your date of birth")

print("Press ANY key to continue")
input()

print("Enter needed information below")

def get_day():
    while True:
        try:
            day = int(input("What day were you born (Number): "))
            return day
        except ValueError:
            print("Invalid input. Please enter a NUMBER.")

def get_month():
    while True:
        try:
            month = int(input("What month were you born in? (Number) "))
            return month
        except ValueError:
            print("Invalid input. Please enter a NUMBER.")

def get_year():
    while True:
        try:
            year = int(input("What year were you born in? "))
            return year
        except ValueError:
            print("Invalid input. Please enter a NUMBER.")

day = get_day()
month = get_month()
year = get_year()

print("Loading...")
time.sleep(3)

print("You were born on: ", day, "/", month, "/", year, "Your age is: ", 2024 - year,)