
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# letters
list_letters = []
for i in range(nr_letters):
    list_letters.append(letters[random.randint(0,len(letters)-1)])

# symbols
list_symbols = []
for i in range(nr_symbols):
    list_symbols.append(symbols[random.randint(0,len(symbols)-1)])

# numbers
list_numbers = []
for i in range(nr_numbers):
    list_numbers.append(numbers[random.randint(0,len(numbers)-1)])

# combine my lists into a 2d array
the_matrix = [list_letters, list_symbols, list_numbers]
my_password = ""

# I know how many items I am going to need so I am just looping that many times. 
for i in range(nr_letters + nr_symbols + nr_numbers):
    # sometimes the lists end up with nothing in them so I am only choosing valid indexes
    valid_choices = []

    # Check to see if we have empty lists
    if list_letters != []:
        valid_choices.append(0)
    
    if list_symbols != []:
        valid_choices.append(1)

    if list_numbers != []:
        valid_choices.append(2)
    
    # it chooses a random index from the ones that are still available
    my_password = my_password + the_matrix[random.choice(valid_choices)].pop()

print("Keep it secret, keep it safe! ~ Gandalf")
print(f"Here is the password: {my_password}")
                

    