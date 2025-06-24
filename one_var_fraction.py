from sympy import symbols, Eq, solve, Rational

# Define the variable
x = symbols('x')

# Define the equation: -5/2x + 3/4x = -7/4
eq = Eq(-Rational(5,2)*x + Rational(3,4)*x, -Rational(7,4))

# Solve for x
solution = solve(eq, x)

print("Solution for x:", solution)