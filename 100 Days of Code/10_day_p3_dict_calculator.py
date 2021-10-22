# incorporating dictionaries
# I really like this solution. Shows the power of dictionaries. 

import os

def get_valid_number():
    invalid_number = True
    while invalid_number:
        number = input("").strip().replace(",", "")
        if number.replace(".", "").isnumeric():
            invalid_number = False
            return float(number)
        else:
            print("Enter a valid number: ")

def get_valid_operation(operations):
    valid_operations = []
    for key in operations:
        valid_operations.append(key)

    invalid_operation = True
    while invalid_operation:
        operation = input("Pick an operation: / * - + ").strip() 
        for i in valid_operations:
            if operation == i:
                invalid_operation = False
                return operation

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    if n2 == 0:
        return "Cant divide by zero!"
    else:
        return n1/n2


end_calculations = False
while not end_calculations:
    os.system('cls' if os.name == 'nt' else 'clear')

    # Making a dictionary of operations
    # I really liked this
    operations = {}

    operations["+"] = add
    operations["-"] = subtract
    operations["*"] = multiply
    operations["/"] = divide

    print("What is the first number? ")
    n1 = get_valid_number()
    operation = get_valid_operation(operations)
    
    print("What is the second number? ")
    n2 = get_valid_number()

    function_from_dict = operations[operation]

    result = function_from_dict(n1, n2)

    print(f"{n1} {operation} {n2} = {result}")

    go_again = input("\nWant to do another calculation? Y or N ").lower()
    if go_again[0] == "n":
        print("Thank you for using the calculator.")
        end_calculations = True


