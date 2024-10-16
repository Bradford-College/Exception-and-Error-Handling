'''
Task 1: Write a Python script that reads a list of numbers from the user. Raise an exception if the user enters a non-numeric value or a negative number.
Task 2: Extend the script to write the valid numbers to a file and handle any IOError exceptions.
'''

'''
Task 1
'''
def get_numbers():
    numbers = []
    while True:
        user_input = input("Enter a number (or type 'done' to finish): ")
        
        if user_input.lower() == 'done':
            break
        
        try:
            num = float(user_input)
            if num < 0:
                raise ValueError("Number cannot be negative.")
            numbers.append(num)
        except ValueError as ve:
            print(f"Invalid input: {ve}")
    
    return numbers

'''
Task 2
'''
def save_to_file(numbers):
    try:
        with open("valid_numbers.txt", "w") as file:
            for num in numbers:
                file.write(f"{num}\n")
        print("Numbers successfully written to file.")
    except IOError:
        print("Error: Could not write to file.")

def get_numbers():
    numbers = []
    while True:
        user_input = input("Enter a number (or type 'done' to finish): ")
        
        if user_input.lower() == 'done':
            break
        
        try:
            num = float(user_input)
            if num < 0:
                raise ValueError("Number cannot be negative.")
            numbers.append(num)
        except ValueError as ve:
            print(f"Invalid input: {ve}")
    
    return numbers

# Main program
numbers = get_numbers()

# Only save if there are valid numbers
if numbers:
    save_to_file(numbers)
else:
    print("No valid numbers to save.")
