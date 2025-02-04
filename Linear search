def linear_search(database, target):
    for index in range(len(database)):
        if database[index] == target:
            return index
    return -1

database = []

while True:
    print("Database Options:")
    print("1. Insert item")
    print("2. Search for item")
    print("3. Close")
    choice = input("Choose a database option: ")

    if choice == "3":
        break
    elif choice == "2":
        target = input("Enter the item you want to search for: ")
        result_index = linear_search(database, target)
        if result_index != -1:
            print(f"Item '{target}' found at index {result_index}.")
        else:
            print(f"Item '{target}' not found in the database.")

    elif choice == "1":
        item = input("Enter the item to add to the database: ")
        database.append(item)
        print(f"Item '{item}' added to the database.")
    else:
        print("Invalid choice. Please choose again.")
