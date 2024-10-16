'''
Write a program that asks the user for two numbers and divides them. 
Handle ZeroDivisionError and ValueError appropriately.
'''
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input, please enter a number.")
