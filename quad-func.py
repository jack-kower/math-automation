import math

def solve_quadratic(a, b, c):
    """Solves ax^2 + bx + c = 0 for x."""
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # No real solutions
    elif discriminant == 0:
        x = -b / (2*a)
        return (x,)
    else:
        sqrt_disc = math.sqrt(discriminant)
        x1 = (-b + sqrt_disc) / (2*a)
        x2 = (-b - sqrt_disc) / (2*a)
        return (x1, x2)

# Example usage:
a = 4
b = 8
c = 7
solutions = solve_quadratic(a, b, c)
print("Solutions:", solutions)