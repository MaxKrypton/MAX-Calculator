from color import Color, colorful_output
from datetime import datetime

class FileManager:
    def __init__(self):
        pass
    
    def save_username_with_timestamp(self, user_name):
        file_name = "/files/usernames.txt"
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open(file_name, "a") as file:
                file.write(f"{user_name} - {current_date}\n")
            colorful_output("Username saved successfully.", Color.GREEN)
        except Exception as e:
            colorful_output(f"Error saving username: {str(e)}", Color.RED)

    def save_history(self, calculator):
        user_name = calculator.get_user_name()
        history = calculator.history
        file_name = f"/files/histories/{user_name}_history.txt"
        try:
            with open(file_name, "a") as file:
                for calculation in history:
                    file.write(calculation + "\n")
            colorful_output("History saved successfully.", Color.GREEN)
        except Exception as e:
            colorful_output(f"Error saving history: {str(e)}", Color.RED)

    def load_history(self, user_name):
        file_name = f"/files/histories/{user_name}_history.txt"
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

def file_management(calculator):
    user_name = calculator.get_user_name()
    file_manager = FileManager()
    while True:
        colorful_output("-" * 50, Color.CYAN)
        colorful_output(f"File Management Menu for {user_name}:", Color.CYAN)
        colorful_output("-" * 50, Color.CYAN)
        print("1. Save History")
        print("2. Load History")
        print("3. Quit")    
        choice = input("> Choose [1/2/3] ")
        if choice == "1":
            if not calculator.history:
                colorful_output("No history to save.", Color.YELLOW)
                continue
            file_manager.save_history(calculator.history, user_name)
        elif choice == "2":
            history = file_manager.load_history(user_name)
            if history:
                colorful_output("Loaded History:", Color.YELLOW)
                for calculation in history:
                    print(calculation.strip())
            else:
                colorful_output("No history found.", Color.YELLOW)
        elif choice == "3":
            break
        else:
            colorful_output("Invalid choice. Please try again.", Color.RED)
