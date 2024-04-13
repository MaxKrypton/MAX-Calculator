from errors import error_handling
from color import Color, colorful_output

class VariableStorage:
    def __init__(self):
        self.variables = {}

    def store_variable(self, name, value):
        self.variables[name] = value
        colorful_output(f"Variable '{name}' stored successfully.", Color.GREEN)

    def retrieve_variable(self, name):
        if name in self.variables:
            return self.variables[name]
        else:
            return f"Error: Variable '{name}' not found."

    def display_variables(self):
        if self.variables:
            colorful_output("Stored Variables:", Color.YELLOW)
            for name, value in self.variables.items():
                print(f"{name}: {value}")
        else:
            colorful_output("No variables stored.", Color.YELLOW)

def variable_storage(calculator):
    storage = VariableStorage()
    while True:
        colorful_output("-" * 30, Color.BLUE)
        colorful_output("Variable Storage Menu:", Color.CYAN)
        colorful_output("-" * 30, Color.BLUE)
        print("1. Store Variable")
        print("2. Retrieve Variable")
        print("3. Display Variables")
        print("00. Go Back")
        choice = input("> Choose [1/2/3/00] ")
        if choice == "1":
            name = input("Enter variable name: ")
            value = input("Enter variable value: ")
            storage.store_variable(name, value)
        elif choice == "2":
            name = input("Enter variable name: ")
            result = storage.retrieve_variable(name)
            colorful_output(result, Color.MAGENTA)
        elif choice == "3":
            storage.display_variables()
        elif choice == "00":
            break
        else:
            error_handling("Invalid choice")
