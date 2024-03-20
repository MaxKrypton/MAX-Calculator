def main():
    print("Welcome to MAX-Calculator")
    
    name = input("What is Your Name? ").strip().title().rstrip()
    
    with open("user_name.txt", "a") as file:
        
        file.write(f"User Name: {name}\n")
    
    print("...............")
    
    print(f"Your name is {name}, You have a wonderful name")

    print("-----------------------------------")
    while True:
        print(f"What is the operation you would like to do, {name}?\n 1. Addtion \n 2. Substration\n 3. Multiplication\n 4. Division\n 5. Power\n 6. Root\n 7. Modulus\n 8. Quit the Program")
        
        # Defining Operation Functions
        def addition(n,m):
            return n + m

        def substraction(n,m):
            return n - m

        def multiplication(n,m):
            return n * m

        def division(n,m):
            return n / m
        
        def power(n, m):
            return n ** m
        
        def root(n, m):
            return n ** (1 / m)

        print("------------------------")

        try:
            choice = int(input("> Choose [1/2/3/4/5/6/7/8] "))
            
            # Addittion Operation

            if choice == 1:
                print("Welcome to the addition operation\n")
                
                x = int(input("What is your first number? "))
                print("...........")
                y = int(input("What is your second number? "))
                print("...........")
                answer = addition(x,y)
                
                print(f"The Sum of {x} and {y} is {answer:,}")
                
            # Substraction Operation
            
            elif choice == 2:
                print("Welcome to the substration operation\n")
                
                x = int(input("What is your first number? "))
                print("...........")
                y = int(input("What is your second number? "))
                print("...........")
                answer = substraction(x,y)
                
                print(f"The Substraction of {x} and {y} is {answer:,}")
                
            # Multiplication Operation
                
            elif choice == 3:
                print("Welcome to the multiplication operation\n")
                
                x = int(input("What is your first number? "))
                print("...........")
                y = int(input("What is your second number? "))
                print("...........")
                answer = multiplication(x,y)
                
                print(f"The Multiplication of {x} and {y} is {answer:,}")
                
            # Division Operation

            elif choice == 4:
                print("Welcome to the division operation\n")
                
                x = int(input("What is your first number? "))
                print("...........")
                y = int(input("What is your second number? "))
                print("...........")
                answer = division(x,y)
                
                print(f"The Divion of {x} and {y} is {answer:,}")
                
            # Power Operation
            
            elif choice == 5:
                print("Welcome to the Power operation\n")
                
                x = int(input("What is the number you want to power? "))
                print("...........")
                y = int(input("What is the power you want to raise the number to? "))
                print("...........")
                answer = power(x,y)
                
                print(f"{x} raised to the power of {y} is eaqual to {answer:,}")
                
            # Square Root
            
            elif choice == 6:
                print("Welcome to the Root operation\n")
                
                x = int(input("What is the number? "))
                print("...........")
                y = int(input("What is the root of your number "))
                print("...........")
                answer = root(x,y)
                
                print(f"The {y} root of {x} is eaqual to {answer:,}")

            elif choice == 7:
                print("Welcome to the Modulus operation\n")
                
                x = int(input("What is your first number? "))
                print("...........")
                y = int(input("What is your second number? "))
                print("...........")
                answer, remainder = modulus(x, y)
                
                print(f"The Modulus of {x} divided by {y} is {answer} with a remainder of {remainder}")

                
            # Quitting the Program
                
            elif choice == 8:
                break
                exit
                
            else:
                print('..............')
                print("ERROR:Please Enter a number between 1 and 4")

        except ValueError:
            print("...............")
            print("Wrong Input: Enter a Valid Number")
        
if __name__=="__main__":
    main()
    