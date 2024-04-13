from calculator import Calculator
from basic import basic_operations_menu
from color import colorful_output
from menu import interactive_menu
from input import dynamic_input_handling
from history import command_history_menu
from settings import settings_management
from help import help_documentation
from evaluator import expression_evaluation
from errors import error_handling
from conversion import unit_conversion
from variables import variable_storage
from file import file_management

def main():
    calculator = Calculator()

    while True:
        # Display interactive menu
        interactive_menu()

        # Get user input
        choice = dynamic_input_handling()

        # Execute chosen option
        if choice == "1":
            basic_operations_menu(calculator)
        elif choice == "2":
            expression_evaluation(calculator)
        elif choice == "3":
            unit_conversion(calculator)
        elif choice == "4":
            variable_storage(calculator)
        elif choice == "5":
            command_history_menu()
        elif choice == "6":
            settings_management()
        elif choice == "7":
            help_documentation()
        elif choice == "8":
            return False  # Exit the calculator
        else:
            error_handling("Invalid choice")

    # Save calculation history to file
    file_manager.save_history(calculator.history, calculator.user_name)

if __name__ == "__main__":
    main()
