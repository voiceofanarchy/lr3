def add(num1, num2):
    try:
        result = float(num1) + float(num2)
        return result
    except ValueError:
        if not is_float(num1) and not is_float(num2):
            return "Invalid input: Both inputs are not numbers"
        elif not is_float(num1):
            return "Invalid input: First input is not a number"
        else:
            return "Invalid input: Second input is not a number"

def subtract(num1, num2):
    try:
        result = float(num1) - float(num2)
        return result
    except ValueError:
        if not is_float(num1) and not is_float(num2):
            return "Invalid input: Both inputs are not numbers"
        elif not is_float(num1):
            return "Invalid input: First input is not a number"
        else:
            return "Invalid input: Second input is not a number"

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
