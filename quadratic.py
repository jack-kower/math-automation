import math
from fractions import Fraction

def solve_quadratic(a, b, c):
    """Solves ax^2 + bx + c = 0 and returns the real roots as a tuple."""
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2*a)
        return (root,)
    else:
        return ()

if __name__ == "__main__":
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        roots = solve_quadratic(a, b, c)
        if roots:
            print("Real roots:", roots)
        else:
            print("No real roots.")
    except Exception as e:
        print("Error:", e)

        def solve_quadratic_fraction(a, b, c):
            """Solves ax^2 + bx + c = 0 and returns the real roots as Fractions."""
            if a == 0:
                raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")
            discriminant = b**2 - 4*a*c
            if discriminant > 0:
                sqrt_disc = math.sqrt(discriminant)
                root1 = Fraction(-b + sqrt_disc, 2*a).limit_denominator()
                root2 = Fraction(-b - sqrt_disc, 2*a).limit_denominator()
                return (root1, root2)
            elif discriminant == 0:
                root = Fraction(-b, 2*a).limit_denominator()
                return (root,)
            else:
                return ()

        if __name__ == "__main__":
            try:
                a = float(input("Enter coefficient a: "))
                b = float(input("Enter coefficient b: "))
                c = float(input("Enter coefficient c: "))
                roots = solve_quadratic(a, b, c)
                if roots:
                    print("Real roots:", roots)
                    frac_roots = solve_quadratic_fraction(a, b, c)
                    print("Real roots as fractions:", frac_roots)
                else:
                    print("No real roots.")
            except Exception as e:
                print("Error:", e)
                def solve_quadratic_fraction(a, b, c):
                    """Solves ax^2 + bx + c = 0 and returns the real roots as Fractions."""
                    if a == 0:
                        raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")
                    discriminant = b**2 - 4*a*c
                    if discriminant > 0:
                        sqrt_disc = math.sqrt(discriminant)
                        root1 = Fraction.from_float((-b + sqrt_disc) / (2*a)).limit_denominator()
                        root2 = Fraction.from_float((-b - sqrt_disc) / (2*a)).limit_denominator()
                        return (root1, root2)
                    elif discriminant == 0:
                        root = Fraction.from_float(-b / (2*a)).limit_denominator()
                        return (root,)
                    else:
                        return ()

                if __name__ == "__main__":
                    try:
                        a = float(input("Enter coefficient a: "))
                        b = float(input("Enter coefficient b: "))
                        c = float(input("Enter coefficient c: "))
                        roots = solve_quadratic(a, b, c)
                        if roots:
                            print("Real roots:", roots)
                            frac_roots = solve_quadratic_fraction(a, b, c)
                            print("Real roots as fractions:", frac_roots)
                        else:
                            print("No real roots.")
                    except Exception as e:
                        print("Error:", e)