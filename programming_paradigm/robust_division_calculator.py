
def safe_divide(numerator, denominator):
    try:
        x = numerator
        y = denominator
        if y == 0:
         return "Error: Cannot divide by zero"
        elif y != int or y != float:
         return "Error: Please enter numeric values only."
        else:
         return x / y
    except ValueError:
        return "Error: Please enter numeric values only."
