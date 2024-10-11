import time, datetime

print("ONLY ENTER NUMBERS")

day = int(input("Enter the day you were born in: "))
month = int(input("Enter the month you were born in: "))
year = int(input("Enter the year you were born in: "))

now = datetime.datetime.now()

print("Thinking...")
time.sleep(3)

print("You are: ")

age = year - now
print("age")