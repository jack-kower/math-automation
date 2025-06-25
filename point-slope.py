# point-slope.py
# y2 - y1 = m * (x2 - x1)

def point_slope_form(m, x1, y1):
    """
    Returns the point-slope form equation as a string: y - y1 = m(x - x1)
    """
    return f"y - {y1} = {m}(x - {x1})"


def parallel_line_equation(m, x1, y1):
    """
    Given a slope m and a point (x1, y1), returns the equation of the line
    parallel to the original with slope m passing through (x1, y1).
    """
    return point_slope_form(m, x1, y1)

# Example usage:
# Original equation: y = 2x + 3 (slope m = 2)
# Point: (4, 5)


if __name__ == "__main__":
    m = .5
    x1, y1 = (1,3)
    eq = parallel_line_equation(m, x1, y1)
    print("Equation of parallel line in point-slope form:")
    print(eq)
    # Convert to y = mx + b form
    b = y1 - m * x1
    print(f"Equation of parallel line in slope-intercept form: y = {m}x + {b}")

