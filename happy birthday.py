import time, datetime

print("This is a python code to say happy birthday once you put your date of birth")

print("Press ANY key to continue")
input()

print("Enter needed information below")

# Functions to get day, month, year input
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
            month = int(input("What month were you born in? (Number): "))
            return month
        except ValueError:
            print("Invalid input. Please enter a NUMBER.")

#This asks for a user to enter the year they were born in
def get_year():
    while True:
        try:
            year = int(input("What year were you born in? "))
            return year #This makes it go back to the start of the def
        except ValueError: #This ignores the error
            print("Invalid input. Please enter a NUMBER.")

# Get user inputs
day = get_day()
month = get_month()
year = get_year()

# Current date
now = datetime.datetime.now()

# Calculate age
birth_date = datetime.datetime(year, month, day)
age = now.year - birth_date.year

# Adjust age if birthday hasn't passed yet this year
if (now.month, now.day) < (birth_date.month, birth_date.day):
    age -= 1

# Display birthdate and age
print("Loading...")
time.sleep(3)
print(f"You were born on: {day}/{month}/{year}. Your age is: {age}")

