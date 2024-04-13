from color import Color, colorful_output


def interactive_menu():
    colorful_output("-" * 30, Color.BLUE)
    colorful_output("Calculator Menu:", Color.BLUE)
    colorful_output("-" * 30, Color.BLUE)
    print("1. Basic Operations")
    print("2. Expression Evaluation")
    print("3. Unit Conversion")
    print("4. Variable Storage")
    print("5. Command History")
    print("6. History Management")
    print("7. Help Documentation")
    print("8. Quit")
