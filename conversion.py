from errors import error_handling
from color import Color, colorful_output


def unit_conversion(calculator):
    colorful_output("*" * 50, Color.BLUE)
    colorful_output("               Unit Conversion Menu", Color.BLUE)
    colorful_output("*" * 50, Color.BLUE)

    print("1. Length")
    print("2. Mass")
    print("3. Volume")
    print("00. Go back")

    choice = input("Enter your choice: ")

    if choice == "1":
        length_conversion(calculator)
    elif choice == "2":
        mass_conversion(calculator)
    elif choice == "3":
        volume_conversion(calculator)
    elif choice == "00":
        return  # Go back
    else:
        error_handling("Invalid choice")


def length_conversion(calculator):
    colorful_output("*" * 50, Color.GREEN)
    colorful_output("        Length Conversion Menu", Color.GREEN)
    colorful_output("*" * 50, Color.GREEN)
    print("1. Meter to Feet")
    print("2. Feet to Meter")
    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            meter = float(input("Enter length in meters: "))
            feet = meter * 3.28084
            colorful_output(f"{meter} meters is equal to {feet:.2f} feet.", Color.CYAN)
            calculator.history.append(f"{meter} meters converted to {feet:.2f} feet")
        except ValueError:
            error_handling("Invalid input")
    elif choice == "2":
        try:
            feet = float(input("Enter length in feet: "))
            meter = feet / 3.28084
            colorful_output(f"{feet} feet is equal to {meter:.2f} meters.", Color.CYAN)
            calculator.history.append(f"{feet} feet converted to {meter:.2f} meters")
        except ValueError:
            error_handling("Invalid input")
    else:
        error_handling("Invalid choice")


def mass_conversion(calculator):
    colorful_output("*" * 50, Color.BLUE)
    colorful_output("         Mass Conversion Menu", Color.BLUE)
    colorful_output("*" * 50, Color.BLUE)
    print("1. Kilogram to Pound")
    print("2. Pound to Kilogram")
    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            kg = float(input("Enter mass in kilograms: "))
            pound = kg * 2.20462
            colorful_output(f"{kg} kilograms is equal to {pound:.2f} pounds.", Color.CYAN)
            calculator.history.append(f"{kg} kilograms converted to {pound:.2f} pounds")
        except ValueError:
            error_handling("Invalid input")
    elif choice == "2":
        try:
            pound = float(input("Enter mass in pounds: "))
            kg = pound / 2.20462
            colorful_output(f"{pound} pounds is equal to {kg:.2f} kilograms.", Color.CYAN)
            calculator.history.append(f"{pound} pounds converted to {kg:.2f} kilograms")
        except ValueError:
            error_handling("Invalid input")
    else:
        error_handling("Invalid choice")


def volume_conversion(calculator):
    colorful_output("*" * 50, Color.MAGENTA)
    colorful_output("       Volume Conversion Menu", Color.MAGENTA)
    colorful_output("*" * 50, Color.MAGENTA)
    print("1. Liter to Gallon")
    print("2. Gallon to Liter")
    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            liter = float(input("Enter volume in liters: "))
            gallon = liter * 0.264172
            colorful_output(f"{liter} liters is equal to {gallon:.2f} gallons.", Color.CYAN)
            calculator.history.append(f"{liter} liters converted to {gallon:.2f} gallons")
        except ValueError:
            error_handling("Invalid input")
    elif choice == "2":
        try:
            gallon = float(input("Enter volume in gallons: "))
            liter = gallon / 0.264172
            colorful_output(f"{gallon} gallons is equal to {liter:.2f} liters.", Color.CYAN)
            calculator.history.append(f"{gallon} gallons converted to {liter:.2f} liters")
        except ValueError:
            error_handling("Invalid input")
    else:
        error_handling("Invalid choice")
