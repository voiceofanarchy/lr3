def add(num1, num2):
    try:
        result = float(num1) + float(num2)
        return result
    except ValueError:
        return "Invalid input"

def subtract(num1, num2):
    try:
        result = float(num1) - float(num2)
        return result
    except ValueError:
        return "Invalid input"
