import math
from errors import error_handling
from color import Color, colorful_output


def expression_evaluation(calculator):
    try:
        colorful_output("-" * 30, Color.BLUE)
        colorful_output("Expression Evaluation:", Color.BLUE)
        colorful_output("-" * 30, Color.BLUE)
        expression = input("Enter an expression: ")
        result = evaluate_expression(expression)
        result_in_message = f"{expression} = {result}"
        colorful_output(result_in_message, Color.GREEN)
        calculator.history.append(f"{expression} = {result}")

    except Exception as e:
        error_handling(str(e))


def evaluate_expression(expression):
    return eval(expression)
