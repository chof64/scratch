retry = True
firstRun = True


def parseOperation(input):
    input = input.lower()

    addition = ["addition", "add", "sum", "plus", "+"]
    subtraction = ["subtraction", "subtract", "minus", "-"]
    multiplication = ["multiplication", "multiply", "times", "*"]
    division = ["division", "divide", "over", "/"]

    if input in addition:
        return "add"
    if input in subtraction:
        return "subtract"
    if input in multiplication:
        return "multiply"
    if input in division:
        return "divide"
    print("\nInvalid operation. Please try again.")
    return ""


def numCheck(input):
    try:
        return float(input)
    except ValueError:
        print("\nInvalid number. Please try again.")
        return ""


def performOperation(operation, num1, num2):
    try:
        if operation == "add":
            return num1 + num2
        if operation == "subtract":
            return num1 - num2
        if operation == "multiply":
            return num1 * num2
        if operation == "divide":
            return num1 / num2
    except ZeroDivisionError:
        print("\nCannot divide by zero. Please try again.")
        return "!!ERROR!!"
    except:
        print("\nAn unknown error has occured. Please try again.")
        return "!!ERROR!!"


def validateRetry(input):
    input = input.lower()
    if input == "y" or input == "yes":
        return True
    if input == "n" or input == "no":
        print("Thank you.")
        return False
    print("\nInvalid input. Program will be terminated.")
    print("Thank you.")
    return False


while retry == True:
    operation = ""
    num1 = ""
    num2 = ""

    if firstRun == True:
        print("Welcome to this simple calculator.")
        print(
            """INSTRUCTIONS:
        This calculator can perform the following operations:
        \t- Addition (+)
        \t- Subtraction (-)
        \t- Multiplication (*)
        \t- Division (/)
        """
        )
        firstRun = False

    while operation == "":
        operation = parseOperation(
            input("Please enter the operation you would like to perform: ")
        )

    while num1 == "":
        num1 = numCheck(input("Please enter the first number: "))
    while num2 == "":
        num2 = numCheck(input("Please enter the second number: "))

    print(f"The result is: " + str(performOperation(operation, num1, num2)))

    retry = validateRetry(input("Would you like to perform another operation? (y/n) "))
