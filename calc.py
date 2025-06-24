x_co = input("Enter the coefficient for x: ")
y_co = input("Enter the coefficient for y: ")

# Convert if valid numbers (including negatives and decimals)
try:
    x_co = float(x_co)
    y_co = float(y_co)
except ValueError:
    print("Please enter valid numbers for x and y coefficients.")
    exit()

x = input("Enter the value for x (or leave blank to solve for y): ")
y = input("Enter the value for y (or leave blank to solve for x): ")

right_side = input("Enter the right side of the equation: ")
try:
    right_side = float(right_side)
except ValueError:
    print("Please enter a valid number for the right side.")
    exit()

# Solve
if x != "" and y == "":
    try:
        x = float(x)
        y = (right_side - x_co * x) / y_co
        print(f"Solved for y: {y}")
    except ZeroDivisionError:
        print("Cannot divide by zero while solving for y.")
elif y != "" and x == "":
    try:
        y = float(y)
        x = (right_side - y_co * y) / x_co
        print(f"Solved for x: {x}")
    except ZeroDivisionError:
        print("Cannot divide by zero while solving for x.")
else:
    print("Please provide exactly one of x or y to solve the equation.")
