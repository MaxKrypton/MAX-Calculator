from color import Color, colorful_output


class CommandHistory:
    def __init__(self):
        self.history = []

    def add_to_history(self, calculation):
        self.history.append(calculation)
        colorful_output("Calculation added to history.", Color.GREEN)

    def clear_history(self):
        self.history = []
        colorful_output("Command history cleared.", Color.RED)

    def display_history(self):
        if self.history:
            colorful_output("Command History:", Color.YELLOW)
            for index, calculation in enumerate(self.history, start=1):
                print(f"{index}. {calculation}")
        else:
            colorful_output("Command History is empty.", Color.YELLOW)


def command_history_menu():
    history = CommandHistory()
    while True:
        colorful_output("-" * 30, Color.CYAN)
        colorful_output("Command History Menu:", Color.CYAN)
        colorful_output("-" * 30, Color.CYAN)
        print("1. Add to History")
        print("2. Clear History")
        print("3. Display History")
        print("00. Go Back")
        choice = input("> Choose [1/2/3/00] ")
        if choice == "1":
            calculation = input("Enter calculation to add to history: ")
            history.add_to_history(calculation)
        elif choice == "2":
            history.clear_history()
        elif choice == "3":
            history.display_history()
        elif choice == "00":
            break
        else:
            colorful_output("Invalid choice. Please try again.", Color.RED)
