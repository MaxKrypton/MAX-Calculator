from errors import error_handling

def dynamic_input_handling():
    while True:
        user_input = input("Enter your choice: ").strip()
        if user_input.isdigit():
            return user_input
        else:
            error_handling("Please enter a valid number.")
