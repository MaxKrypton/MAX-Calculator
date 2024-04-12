class Calculator:
    def __init__(self):
        self.user_name = ""
    
    def set_user_name(self, name):
        self.user_name = name.strip().title().rstrip()
        
    def addition(self, n, m):
        return n + m

    def subtraction(self, n, m):
        return n - m

    def multiplication(self, n, m):
        return n * m

    def division(self, n, m):
        return n / m

    def power(self, n, m):
        return n ** m

    def root(self, n, m):
        return n ** (1 / m)

    def modulus(self, n, m):
        quotient = n // m
        remainder = n % m
        return quotient, remainder

    def run_calculator(self):
        print("Welcome to MAX-Calculator")
        self.set_user_name(input("What is Your Name? "))
        print(f"Your name is {self.user_name}, You have a wonderful name")
        print("-----------------------------------")

        while True:
            print(f"What is the operation you would like to do, {self.user_name}?\n"
                  "1. Addition\n"
                  "2. Subtraction\n"
                  "3. Multiplication\n"
                  "4. Division\n"
                  "5. Power\n"
                  "6. Root\n"
                  "7. Modulus\n"
                  "8. Quit the Program")

            try:
                choice = int(input("> Choose [1/2/3/4/5/6/7/8] "))

                if choice == 8:
                    break

                x = int(input("What is your first number? "))
                y = int(input("What is your second number? "))

                if choice == 1:
                    print(f"The Sum of {x} and {y} is {self.addition(x, y):,}")
                elif choice == 2:
                    print(f"The Subtraction of {x} and {y} is {self.subtraction(x, y):,}")
                elif choice == 3:
                    print(f"The Multiplication of {x} and {y} is {self.multiplication(x, y):,}")
                elif choice == 4:
                    print(f"The Division of {x} and {y} is {self.division(x, y):,}")
                elif choice == 5:
                    print(f"{x} raised to the power of {y} is equal to {self.power(x, y):,}")
                elif choice == 6:
                    print(f"The {y}-th root of {x} is equal to {self.root(x, y):,}")
                elif choice == 7:
                    quotient, remainder = self.modulus(x, y)
                    print(f"The Modulus of {x} divided by {y} is {quotient} with a remainder of {remainder}")

            except ValueError:
                print("ERROR: Please Enter a valid number between 1 and 8")


if __name__ == "__main__":
    calc = Calculator()
    calc.run_calculator()
