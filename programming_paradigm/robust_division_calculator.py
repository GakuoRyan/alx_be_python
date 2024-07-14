
def safe_divide(numerator, denominator):
    try:
        x = float(numerator)
        y = float(denominator)
        if y == 0:
           return  "Error: Cannot divide by zero."
        return f"The result of the division is {x / y:.1f}"
    except ValueError:
        return "Error: Please enter numeric values only."
