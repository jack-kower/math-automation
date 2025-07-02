x = 'x'
n = input("Enter the exponent n (can be decimal): ")
r = input("Enter the equality (x^n = r): ")

# Convert n
try:
    n = float(n)
except ValueError:
    print("Invalid input. Please enter a number for the exponent.")
    exit()

# Convert r
try:
    r = float(r)
except ValueError:
    print("Invalid input. Please enter a number for the equality.")
    exit()

# Handle special case
if n == 0:
    if r == 1:
        print("Any x is a solution (x^0 = 1 for x ≠ 0).")
    else:
        print("No solution (x^0 = 1 for any x ≠ 0).")
else:
    try:
        x_val = r ** (1 / n)
        print(f"x = {x_val}")
    except ValueError:
        # Try complex result if math domain error
        import cmath
import math
        x_val = cmath.exp(cmath.log(r) / n)
        print(f"x is a complex number: x = {x_val}")

        # Check for additional real roots if n is even and r is negative

        if n % 2 == 0 and r < 0:
            print("No real solution since even root of negative number is not real.")
            x_val = cmath.exp(cmath.log(r) / n)
            print(f"x is a complex number: x = {x_val}")
        elif n != 0 and (r < 0 and n % 2 != 0):
            # Odd root of negative number is real
            x_val = -((-r) ** (1 / n))
            print(f"x = {x_val}")

