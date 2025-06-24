from sympy import symbols, Eq, solve, Rational

# Example equation: (1/3)x + (1/2) = (3/4)
x = symbols('x')
equation = Eq(Rational(1, 3)*x + Rational(1, 2), Rational(3, 4))

solution = solve(equation, x)
print("Solution for x:", solution)