from color import Color, colorful_output

class SettingsManager:
    def __init__(self):
        self.number_format = "standard"
        self.decimal_precision = 2
        self.default_behavior = "basic"

    def display_settings(self):
        colorful_output("Current Settings:", Color.YELLOW)
        print(f"Number Format: {self.number_format}")
        print(f"Decimal Precision: {self.decimal_precision}")
        print(f"Default Behavior: {self.default_behavior}")

    def update_settings(self, number_format, decimal_precision, default_behavior):
        self.number_format = number_format
        self.decimal_precision = decimal_precision
        self.default_behavior = default_behavior
        colorful_output("Settings updated successfully.", Color.GREEN)

def settings_management():
    settings = SettingsManager()
    while True:
        colorful_output("-" * 30, Color.CYAN)
        colorful_output("Settings Menu:", Color.CYAN)
        colorful_output("-" * 30, Color.CYAN)
        print("1. Display Settings")
        print("2. Update Settings")
        print("00. Go Back")
        choice = input("> Choose [1/2/00] ")
        if choice == "1":
            settings.display_settings()
        elif choice == "2":
            number_format = input("Enter number format [standard/scientific]: ")
            decimal_precision = int(input("Enter decimal precision: "))
            default_behavior = input("Enter default behavior [basic/advanced]: ")
            settings.update_settings(number_format, decimal_precision, default_behavior)
        elif choice == "00":
            break
        else:
            colorful_output("Invalid choice. Please try again.", Color.RED)
