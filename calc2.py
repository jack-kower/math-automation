x = 0
y = ""
x_coor = 0
y_coor = 0
right_side = 0

right_side = x_coor * x + y_coor * y
if x != "" and y == "":
    try:
        x = float(x)
        y = (right_side - x_coor * x) / y_coor
        print(f"Solved for y: {y}")
    except ZeroDivisionError:
        print("Cannot divide by zero while solving for y.")