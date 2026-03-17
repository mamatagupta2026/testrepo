# Program to add two numbers with input validation
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    total = num1 + num2
    print(f"The sum of {num1} and {num2} is {total}")
except ValueError:
    print("Invalid input! Please enter numeric values.")
    print("Invalid input.")
