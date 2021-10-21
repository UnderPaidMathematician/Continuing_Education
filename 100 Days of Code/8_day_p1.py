# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello!")
    print("How are,")
    print("you today?")

greet()

# pass variables
def greet_with_name(name):
    print(f"Hello, {name}")
    print(f"How do you do {name}?")

greet_with_name("Jason")

# Multi variables
def greet_with_name_and_location(name, location):
    print(f"Hello, {name} how is the weather in {location}?")

greet_with_name_and_location(name="Jason", location="Forest, VA")