class CustomError(Exception):
    pass

def check_even(number):
    if number % 2 != 0:
        raise CustomError("This number is not even.")
    return number
check_even(1)