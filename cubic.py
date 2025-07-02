import numpy as np

def solve_cubic(a, b, c, d):
    """
    Solves the cubic equation: a*x^3 + b*x^2 + c*x + d = 0
    Returns a list of real roots.
    """
    if a == 0:
        # Degenerates to quadratic
        coeffs = [b, c, d]
    else:
        coeffs = [a, b, c, d]
    roots = np.roots(coeffs)
    # Return only real roots
    real_roots = [r.real for r in roots if np.isreal(r)]
    return real_roots

# Example usage:
if __name__ == "__main__":
    # Example: x^3 - 6x^2 + 11x - 6 = 0  (roots: 1, 2, 3)
    a, b, c, d = 2, -26, 84, 0
    roots = solve_cubic(a, b, c, d)
    print("Real roots:", roots)