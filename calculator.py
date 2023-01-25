# This function performs the requested operation
def perform_operation(choice, num1, num2):
    operations = {
        '1': lambda: num1 + num2,
        '2': lambda: num1 - num2,
        '3': lambda: num1 * num2,
        '4': lambda: num1 / num2,
    }
    try:
        result = operations[choice]()
    except KeyError:
        print("Invalid choice. Please select a number between 1 and 4.")
        return
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return
    print(f"{num1} {choice} {num2} = {result}")

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4) or Q to quit: ")
    if choice.upper() == "Q":
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    perform_operation(choice, num1, num2)