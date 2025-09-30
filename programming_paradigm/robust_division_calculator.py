# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divides two numbers.
    Handles errors for division by zero and non-numeric input.
    """

    try:
        # convert inputs to float (may raise ValueError)
        num = float(numerator)
        den = float(denominator)

        # attempt division (may raise ZeroDivisionError)
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
