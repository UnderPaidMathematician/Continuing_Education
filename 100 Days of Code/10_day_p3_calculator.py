# This was my solution for a calculator 
# It looked like hers was going to be basic but now I see she is storing her functions in a dictionary. 
# Im going to redo this code to see what she is doing. Though this code worked perfectly.

import os

def get_valid_number():
    invalid_number = True
    while invalid_number:
        number = input("").strip().replace(",", "")
        if number.replace(".","").isnumeric():
            invalid_number = False
            return float(number)
        else:
            print("Enter a valid number: ")

def get_valid_operation():
    valid_operations = ["/","*","-","+"]

    invalid_operation = True
    while invalid_operation:
        operation = input("Pick an operation: / * - + ").strip() 
        for i in valid_operations:
            if operation == i:
                invalid_operation = False
                return operation



def calculate(first_number, second_number, operation):
    if operation == "+":
        return n1 + n2
    elif operation == "-":
        return n1 - n2
    elif operation == "*":
        return n1*n2
    elif operation == "/" and n2 != 0:
        return n1/n2
    elif operation == "/" and n2 == 0:
        return "Cant divide by zero"


end_calculations = False
while not end_calculations:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("What is the first number? ")
    n1 = get_valid_number()
    operation = get_valid_operation()
    print("What is the second number? ")
    n2 = get_valid_number()


    result = calculate(first_number=n1, second_number=n1, operation=operation)

    print(f"{n1} {operation} {n2} = {result}")

    go_again = input("\nWant to do another calculation? Y or N ").lower()
    if go_again[0] == "n":
        print("Thank you for using the calculator.")
        end_calculations = True


