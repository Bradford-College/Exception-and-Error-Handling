try:
    x = int(input("Enter a number: "))
    y = 10 / x
    print(y)
except (ZeroDivisionError, ValueError) as e:
    print(f"An error occurred: {e}")