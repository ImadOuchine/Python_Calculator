print("calculator".upper())

operations = {
    "+": "addition",
    "-": "subtraction",
    "*": "multiplication",
    "/": "division"
}

for symbol, name in operations.items():
    print(name, ":", symbol)


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Cannot divide by zero")


while True:

    the_choose = input("Please enter your choice: ").lower()

    while True:
        try:
            if the_choose == "addition" or the_choose == "+":
                num1 = int(input("Enter your first number: "))
                num2 = int(input("Enter your second number: "))
                print(add(num1, num2))
                break

            elif the_choose == "subtraction" or the_choose == "-":
                num1 = int(input("Enter your first number: "))
                num2 = int(input("Enter your second number: "))
                print(sub(num1, num2))
                break

            elif the_choose == "multiplication" or the_choose == "*":
                num1 = int(input("Enter your first number: "))
                num2 = int(input("Enter your second number: "))
                print(mul(num1, num2))
                break

            elif the_choose == "division" or the_choose == "/":
                num1 = int(input("Enter your first number: "))
                num2 = int(input("Enter your second number: "))
                div(num1, num2)
                break

            else:
                print("Please enter a valid choice")
                break

        except ValueError:
            print("Please enter a number, not a letter")

