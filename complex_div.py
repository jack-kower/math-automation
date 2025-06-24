def divide_complex(a, b):
    """
    Divide two complex numbers a and b.
    :param a: complex, numerator
    :param b: complex, denominator
    :return: complex, result of a / b
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    # Example usage
    num1 = complex(input("Enter first complex number (e.g. 1+2j): "))
    num2 = complex(input("Enter second complex number (e.g. 3-4j): "))
    try:
        result = divide_complex(num1, num2)
        print(f"({num1}) / ({num2}) = {result}")
    except ZeroDivisionError as e:
        print(e)