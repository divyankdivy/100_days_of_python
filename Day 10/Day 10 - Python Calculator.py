def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    from art import calculator_logo
    from art import calculator_art
    print(calculator_logo)
    print(calculator_art)
    num1 = float(input("Enter the number: "))
    for symbol in operations:
        print(symbol)

    end_calculation = False
    while not end_calculation:
        operation = input("Choose an operation: ")
        num2 = float(input("Enter the number: "))
        op_func = operations[operation]
        answer = op_func(num1,num2)
        print(f"{num1} {operation} {num2} = {answer}")
        cal_choice = input("Would you like to continue with the current calculation? 'y','n' or 'new': ")
        if cal_choice == 'y':
            num1 = answer
        elif cal_choice == 'n':
            end_calculation = True
            print("Thanks for using the Python Calculator!")
        elif cal_choice == 'new':
            end_calculation = True
            calculator()

calculator()
