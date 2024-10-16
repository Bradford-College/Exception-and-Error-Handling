'''
Write a function that takes a number as input. 
Raise a custom exception if the number is negative.
'''
class NegativeNumberError(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise NegativeNumberError("The number is negative!")
    return number

try:
    num = int(input("Enter a positive number: "))
    check_positive(num)
    print(f"The number {num} is valid.")
except NegativeNumberError as e:
    print(e)
except ValueError:
    print("Error: Invalid input, please enter a valid number.")