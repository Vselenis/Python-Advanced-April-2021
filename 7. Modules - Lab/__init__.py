from .operations import add, divide, subtract, power, multiply

def calculation_expression(expression):
    (x, sign, y) = expression.split(" ")
    result = None
    if sign == '+':
        result = add(x, y)
    elif sign == '-':
        result = subtract(x, y)
    elif sign == "/":
        result = divide(x, y)
    elif sign == '*':
        result = multiply(x, y)
    elif sign == "^":
        result = power(x, y)
    else:
        raise Exception(f"Invalid sign {sign}")
    print(result)