from basic_operations import addition, subtraction, multiplication, division, power, root, modulus
from errors import error_handling
from color import Color, colorful_output


def basic_operations_menu(calculator):
    while True:
        colorful_output("-" * 30, Color.BLUE)
        colorful_output("Basic Operations Menu:", Color.BLUE)
        colorful_output("-" * 30, Color.BLUE)
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Root")
        print("7. Modulus")
        print("00. Go back")
        choice = input("Enter your choice: ")

        if choice == "00":
            break
        else:
            perform_basic_operation(choice, calculator)


def perform_basic_operation(choice, calculator):
    operation_functions = {
        "1": addition,
        "2": subtraction,
        "3": multiplication,
        "4": division,
        "5": power,
        "6": root,
        "7": modulus
    }

    operation_function = operation_functions.get(choice)
    if operation_function:
        perform_operation(operation_function, calculator)
    else:
        error_handling("Invalid choice")


def perform_operation(operation_function, calculator):
    try:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = operation_function(x, y)
        result_in_message = f"{x} {operation_function.__name__} {y} = {result}"
        colorful_output(result_in_message, Color.GREEN)
        calculator.history.append(f"{x} {operation_function.__name__} {y} = {result}")
    except ValueError:
        error_handling("Invalid input")
    except Exception as e:
        error_handling(str(e))
