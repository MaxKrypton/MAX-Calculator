from errors import error_handling
from color import Color, colorful_output
from file import save_variables_to_file, load_variables_from_file


class VariableStorage:
    def __init__(self):
        self.variables = load_variables_from_file()

    def store_variable(self, name, value):
        self.variables[name] = value
        save_variables_to_file(self.variables)
        colorful_output(f"Variable '{name}' stored successfully.", Color.GREEN)

    def retrieve_variable(self, name):
        self.variables = load_variables_from_file()
        if name in self.variables:
            return self.variables[name]
        else:
            return f"Error: Variable '{name}' not found."

    def display_variables(self):
        self.variables = load_variables_from_file()
        if self.variables:
            colorful_output("Stored Variables:", Color.YELLOW)
            for name, value in self.variables.items():
                print(f"{name}: {value}")
        else:
            colorful_output("No variables stored.", Color.YELLOW)
    def delete_variable(self, name):
        self.variables = load_variables_from_file()
        if name in self.variables:
            del self.variables[name]
            save_variables_to_file(self.variables)
            colorful_output(f"Variable '{name}' deleted successfully.", Color.RED)
        else:
            colorful_output(f"Error: Variable '{name}' not found.", Color.RED)

def variable_storage(calculator):
    storage = VariableStorage()
    while True:
        colorful_output("-" * 30, Color.BLUE)
        colorful_output("Variable Storage Menu:", Color.CYAN)
        colorful_output("-" * 30, Color.BLUE)
        print("1. Store Variable")
        print("2. Retrieve Variable")
        print("3. Display Variables")
        print("4. Delete Variable")
        print("00. Go Back")
        choice = input("> Choose [1/2/3/4/00] ")
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
                        elif choice == "4":
            name = input("Enter variable name to delete: ")
            storage.delete_variable(name)
        elif choice == "00":
            break
        else:
            error_handling("Invalid choice")

