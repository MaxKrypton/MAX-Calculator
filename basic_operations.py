def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Division by zero")


def power(x, y):
    return x ** y


def root(x, y):
    if x >= 0 and y != 0:
        return x ** (1 / y)
    else:
        raise ValueError("Invalid input for root operation")


def modulus(x, y):
    quotient = x // y
    remainder = x % y
    return quotient, remainder

