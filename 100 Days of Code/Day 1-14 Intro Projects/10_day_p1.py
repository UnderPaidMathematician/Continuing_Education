def format_name(f_name, l_name):
    return f"{f_name} {l_name}".title()

first_name = input("Whats your first name: ")
last_name = input("Whats your last name? ")

name = format_name(first_name, last_name)
print(name)