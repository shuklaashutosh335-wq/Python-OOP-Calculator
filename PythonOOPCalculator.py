# MINOR PROJECT

# "Python OOP Calculator"

# Building a calculator which can perform :
# 1.Addition , 2.Subtraction , 3.Multiplication , 4.Division ,
# 5.percentage , 6.modulus and 7.power operations of two numbers.

# Class for performing calculator operations
class Calculator:

    # Method to perform calculations
    def calculate(self, a, b, choice):

        # Addition
        if choice == "1":
            return a + b

        # Subtraction
        elif choice == "2":
            return a - b

        # Multiplication
        elif choice == "3":
            return a * b

        # Division
        elif choice == "4":
            if b == 0:
                return "Cannot divide by zero!"
            return a / b

        # Percentage (a percent of b)
        elif choice == "5":
            return (a / 100) * b

        # Modulus (remainder)
        elif choice == "6":
            if b == 0:
                return "Cannot divide by zero!"
            return a % b

        # Power (a raised to b)
        elif choice == "7":
            return a ** b


# Creating an object of Calculator class
calc = Calculator()

# Loop to run the calculator repeatedly
while True:

    # Displaying the calculator menu
    print("\n--- CALCULATOR ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Percentage")
    print("6. Modulus")
    print("7. Power")
    print("8. Exit")

    # Taking user's choice
    choice = input("Enter choice: ")

    # Exiting the calculator
    if choice == "8":
        print("Thank you!")
        break

    # Checking whether the choice is valid
    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid choice!")
        continue

    try:
        # Taking two numbers from the user
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        # Calling the calculate method
        result = calc.calculate(a, b, choice)

        # Displaying the final result
        print("Result:", result)

    # Handling invalid number inputs
    except ValueError:
        print("Please enter valid numbers!")

