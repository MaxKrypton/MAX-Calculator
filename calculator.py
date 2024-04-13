from color import Color, colorful_output

class Calculator:
    def __init__(self):
        colorful_output("====================================", Color.BLUE)
        colorful_output("Welcome to the MAX-Calculator!", Color.BLUE)
        colorful_output("====================================", Color.BLUE)
        self.user_name = input("What is your name? ")
        self.history = []

    def save_to_history(self, calculation):
        # Method to save calculation to history
        self.history.append(calculation)

    def clear_history(self):
        # Method to clear calculation history
        self.history = []

    def save_user_name(self, name):
        # Method to save user's name
        self.user_name = name

    def get_user_name(self):
        # Method to get user's name
        return self.user_name
