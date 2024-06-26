import os
from color import Color, colorful_output
from datetime import datetime

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_history(calculator):
    user_name = calculator.get_user_name()
    history = calculator.history
    directory = "./files/histories/"
    ensure_directory_exists(directory)
    file_name = f"{directory}{user_name}_history.txt"
    try:
        with open(file_name, "a") as file:
            for calculation in history:
                file.write(calculation + "\n")
        colorful_output("History saved successfully.", Color.GREEN)
        calculator.clear_history()
    except Exception as e:
        colorful_output(f"Error saving history: {str(e)}", Color.RED)
        
def delete_history(user_name):
    directory = "./files/histories/"
    ensure_directory_exists(directory)
    file_name = f"{directory}{user_name}_history.txt"
    try:
        os.remove(file_name)
        colorful_output("History deleted successfully.", Color.GREEN)
    except FileNotFoundError:
        colorful_output("History file not found.", Color.YELLOW)
    except Exception as e:
        colorful_output(f"Error deleting history: {str(e)}", Color.RED)

def load_history(user_name):
    directory = "./files/histories/"
    ensure_directory_exists(directory)
    file_name = f"{directory}{user_name}_history.txt"
    try:
        with open(file_name, "r") as file:
            history = file.readlines()
        return history
    except FileNotFoundError:
        colorful_output("History file not found.", Color.YELLOW)
        return []
    except Exception as e:
        colorful_output(f"Error loading history: {str(e)}", Color.RED)
        return []

def save_username_with_timestamp(user_name):
    directory = "./files/"
    ensure_directory_exists(directory)
    file_name = f"{directory}usernames.txt"
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(file_name, "a") as file:
            file.write(f"{user_name} , {current_date}\n")
        colorful_output("Username saved successfully.", Color.GREEN)
    except Exception as e:
        colorful_output(f"Error saving username: {str(e)}", Color.RED)

def file_management(calculator):
    user_name = calculator.get_user_name()
    while True:
        colorful_output("-" * 50, Color.CYAN)
        colorful_output(f"History Management Menu for {user_name}:", Color.CYAN)
        colorful_output("-" * 50, Color.CYAN)
        print("1. Save History")
        print("2. Load History")
        print("3. Clear History")
        print("00. Go Back")
        choice = input("> Choose [1/2/3/00] ")
        if choice == "1":
            if not calculator.history:
                colorful_output("No history to save.", Color.YELLOW)
                continue
            save_history(calculator)
        elif choice == "2":
            history = load_history(user_name)
            if history:
                colorful_output("Loaded History:", Color.YELLOW)
                for calculation in history:
                    print(calculation.strip())
            else:
                colorful_output("No history found.", Color.YELLOW)
        elif choice == "3":
            calculator.clear_history()
            delete_history(user_name)
        elif choice == "00":
            break
        else:
            colorful_output("Invalid choice. Please try again.", Color.RED)
        
        # press any key to continue
        input("Press any key to continue...")

def load_variables_from_file():
    variable_storage = {}
    directory = "./files/"
    ensure_directory_exists(directory)
    file_name = f"{directory}variables.txt"
    try:
        with open(file_name, "r") as file:
            for line in file:
                name, value = line.strip().split(" = ")
                variable_storage[name] = value
        return variable_storage
    except FileNotFoundError:
        colorful_output("No variables found.", Color.YELLOW)
        return {}
    except Exception as e:
        colorful_output(f"Error loading variables: {str(e)}", Color.RED)
        return {}

def save_variables_to_file(variable_storage):
    directory = "./files/"
    ensure_directory_exists(directory)
    file_name = f"{directory}variables.txt"
    try:
        with open(file_name, "w") as file:
            for name, value in variable_storage.items():
                file.write(f"{name} = {value}\n")
        colorful_output("Variables saved successfully.", Color.GREEN)
    except Exception as e:
        colorful_output(f"Error saving variables: {str(e)}", Color.RED)

def load_commands_from_file():
    command_storage = []
    directory = "./files/"
    ensure_directory_exists(directory)
    file_name = f"{directory}commands.txt"
    try:
        with open(file_name, "r") as file:
            for line in file:
                command_storage.append(line.strip())
        return command_storage
    except FileNotFoundError:
        colorful_output("No commands found.", Color.YELLOW)
        return []
    except Exception as e:
        colorful_output(f"Error loading commands: {str(e)}", Color.RED)
        return []

def save_commands_to_file(command_storage):
    directory = "./files/"
    ensure_directory_exists(directory)
    file_name = f"{directory}commands.txt"
    try:
        with open(file_name, "w") as file:
            for command in command_storage:
                file.write(f"{command}\n")
        colorful_output("Commands saved successfully.", Color.GREEN)
    except Exception as e:
        colorful_output(f"Error saving commands: {str(e)}", Color.RED)
        
def clear_commands_from_file():
    directory = "./files/"
    ensure_directory_exists(directory)
    file_name = f"{directory}commands.txt"
    try:
        os.remove(file_name)
        colorful_output("Commands deleted successfully.", Color.GREEN)
    except FileNotFoundError:
        colorful_output("Commands file not found.", Color.YELLOW)
    except Exception as e:
        colorful_output(f"Error deleting commands: {str(e)}", Color.RED)

