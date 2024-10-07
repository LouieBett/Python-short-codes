import time

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_option():
    while True:
        option = input("Enter the function (E.g Multiply, Subtract, Addition, Divide): ")
        if option.lower() in ["multiply", "times", "x"]:
            return "multiply"
        elif option.lower() in ["subtract", "takeaway", "minus", "-"]:
            return "subtract"
        elif option.lower() in ["addition", "add", "plus", "+"]:
            return "add"
        elif option.lower() in ["divide", "÷"]:
            return "divide"
        else:
            print("Invalid option. Please enter 'Multiply', 'Subtract', 'Addition', or 'Divide'.")

def main():
    num1 = get_number("Enter number 1: ")
    num2 = get_number("Enter number 2: ")
    option = get_option()

    if option == "multiply":
        result = num1 * num2
    elif option == "subtract":
        result = num1 - num2
    elif option == "add":
        result = num1 + num2
    elif option == "divide":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return

    print("Your answer:", result)

if __name__ == "__main__":
    main()