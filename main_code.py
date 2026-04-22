# ================================
# Synent Technologies Internship
# Name: Ayesha Ansari
# Task: Task 1 - Simple Calculator
# ================================

def Addition(a, b):
    return a + b

def Subtraction(a, b):
    return a - b

def Multiplication(a, b):
    return a * b

def Division(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def start_calculator():
    print("Welcome to Simple Calculator!")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nChoose Operation:")
        print("[1] Addition")
        print("[2] Subtraction")
        print("[3] Multiplication")
        print("[4] Division")

        choice = input("Enter choice (1-4): ")

        if choice == '1':
            print("Result:", Addition(num1, num2))
        elif choice == '2':
            print("Result:", Subtraction(num1, num2))
        elif choice == '3':
            print("Result:", Multiplication(num1, num2))
        elif choice == '4':
            print("Result:", Division(num1, num2))
        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter valid numbers")


start_calculator()