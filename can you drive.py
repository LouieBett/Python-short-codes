age = int(input("How old are you? "))
location = input("Where do you live? ")

if age >=17:
    if location == "UK":
        print("You are",age, "years old you can drive")
    else:
        print("Sorry, your old enough but you dont live in the UK.")
else:
    print("You are",age, "years old You cannot drive")
