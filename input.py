def dynamic_input_handling():
    while True:
        user_input = input("Enter your choice: ").strip()
        if user_input.isdigit():
            return user_input
        else:
            print("Error: Please enter a valid number.")
