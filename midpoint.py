def midpoint(point1, point2):
    """
    Calculate the midpoint between two points in 2D space.

    Args:
        point1 (tuple): The (x, y) coordinates of the first point.
        point2 (tuple): The (x, y) coordinates of the second point.

    Returns:
        tuple: The (x, y) coordinates of the midpoint.
    """
    x_mid = (point1[0] + point2[0]) / 2
    y_mid = (point1[1] + point2[1]) / 2
    return (x_mid, y_mid)

# Example usage:
if __name__ == "__main__":
    p1 = (-3, 7)
    p2 = (3, -11)
    print("Midpoint:", midpoint(p1, p2))