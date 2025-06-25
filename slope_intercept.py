def line_from_point_slope(point, slope):
    """
    Returns the slope-intercept form (y = mx + b) of a line given a point and slope.

    Args:
        point (tuple): A tuple (x1, y1) representing a point on the line.
        slope (float): The slope (m) of the line.

    Returns:
        tuple: (m, b) where y = mx + b
    """
    x1, y1 = point
    m = slope
    b = y1 - m * x1
    return m, b

# Example usage:
# Given point (2, 3) and slope 4
m, b = line_from_point_slope((1, 2), -4/5)
print(f"y = {m}x + {b}")
