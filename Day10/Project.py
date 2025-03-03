value = 0

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    continue_calculation = True
    first_number = float(input("What's is the first number?: "))

    while continue_calculation:
        for key in operations:
            print(key)
        operation = input("Pick an operation: ")
        second_number = float(input("What's is the next number?: "))
        value = operations[operation](first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {value}")
        y_n = input(f"Type 'y' to continue calculating with {value}, or type 'n' to start a new calculation: ").lower()
        if y_n == 'y':
            first_number = value
        else:
            continue_calculation = False
            print("\n" * 20)
            calculator()

calculator()