# Task 1: Simple Calculator
# Objective: Create a simple calculator that performs basic operations (addition, subtraction, multiplication, and division) based on user input.

# Instructions:

# Ask the user to enter two numbers.
# Ask the user to enter an operation (+, -, *, /).
# Perform the operation and display the result.

# Get the first number from the user
num1 = float(input("Enter the first number: "))

# Get the second number from the user
num2 = float(input("Enter the second number: "))

# Get the operation from the user
operation = input("Enter an operation (+, -, *, /): ")

# Perform the operation and display the result
if operation == '+':
    result = num1 + num2
    print(f"The result is: {result}")
elif operation == '-':
    result = num1 - num2
    print(f"The result is: {result}")
elif operation == '*':
    result = num1 * num2
    print(f"The result is: {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"The result is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation entered.")
