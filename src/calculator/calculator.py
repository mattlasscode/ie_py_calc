def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def percentage_change(new: float, old: float) -> float:
    if old == 0:
        raise ValueError("Cannot divide by zero.")
    return (new - old) / old


def compound_growth(start: float, rate: float, periods: float) -> float:
    return start * (1 + rate) ** periods



while True:
    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'percentage_change' to calculate percentage change")
    print("Enter 'compound_growth' to calculate compound growth")
    print("Enter 'quit' to end the program")
    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input == "add":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = add(num1, num2)
        print(result)
    elif user_input == "subtract":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = subtract(num1, num2)
        print(result)
    elif user_input == "multiply":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = multiply(num1, num2)
        print(result)
    elif user_input == "divide":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = divide(num1, num2)
        print(result)
    elif user_input == "percentage_change":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = percentage_change(num1, num2)
        print(result)
    elif user_input == "compound_growth":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        num3 = float(input("Enter another number: "))
        result = compound_growth(num1, num2, num3)
        print(result)
    else:
        print("Unknown input")