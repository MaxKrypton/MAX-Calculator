from color import Color, colorful_output
from file import load_commands_from_file, save_commands_to_file, clear_commands_from_file


class CommandHistory:
    def __init__(self):
        self.command_history = load_commands_from_file()

    def add_to_history(self, calculation):
        self.command_history.append(calculation)
        save_commands_to_file(self.command_history)

    def clear_history(self):
        self.history = []
        clear_commands_from_file()
        colorful_output("Command history cleared.", Color.RED)

    def display_history(self):
        self.history = load_commands_from_file()
        if self.history:
            colorful_output("Command History:", Color.YELLOW)
            for index, calculation in enumerate(self.history, start=1):
                print(f"{index}. {calculation}")
        else:
            colorful_output("Command History is empty.", Color.YELLOW)


def command_history_menu():
    command_history = CommandHistory()
    while True:
        colorful_output("-" * 30, Color.CYAN)
        colorful_output("Command History Menu:", Color.CYAN)
        colorful_output("-" * 30, Color.CYAN)
        print("1. Add to Command History")
        print("2. Clear Command History")
        print("3. Display Command History")
        print("00. Go Back")
        choice = input("> Choose [1/2/3/00] ")
        if choice == "1":
            calculation = input("Enter calculation to add to command history: ")
            command_history.add_to_history(calculation)
        elif choice == "2":
            command_history.clear_history()
        elif choice == "3":
            command_history.display_history()
        elif choice == "00":
            break
        else:
            colorful_output("Invalid choice. Please try again.", Color.RED)
