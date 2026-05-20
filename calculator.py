# Practice Calculator Program

def calculator():
    print("=== Aapo Practice Calculator ===")
    print("You can perform +, -, *, / operations.")
    print("Type 'q' to quit.\n")

    while True:
        choice = input("Enter operation (+, -, *, /) or 'q' to quit: ")

        if choice.lower() == 'q':
            print("Exiting calculator... Goodbye!")
            break

        # Get numbers from user
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        # Perform calculation
        if choice == '+':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == '-':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == '*':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == '/':
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation! Please choose +, -, *, or /.")

# Run the calculator
calculator()
