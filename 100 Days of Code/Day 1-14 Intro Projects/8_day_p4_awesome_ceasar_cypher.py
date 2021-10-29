import os
from art import logo


# Clear the console
os.system('cls' if os.name == 'nt' else 'clear')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#e.g. 
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

# Day 8: I am not really being challenged so I made this more complex. 
# I added uppercase letters and used ordinal values for characters in the alphabet.

# text = text to be cyphered
# encrypt True encrypts the text
# encrypt False decrypts the text
# Shift is the agreed upon offset
def encrypt_decrypt(text, encrypt, shift):

    # return a list of uppercase values
    uppercase = [x.upper() for x in alphabet]

    # Extend the values onto the list
    # I really like this function I did not know about extend before this course
    alphabet.extend(uppercase)

    # Change ascii to its ordinal code equivelent
    ord_alpha = [ord(c) for c in alphabet]

    '''
    # This dictionary was not used in the end. 
    # I had printed it so I could see what the ordinal values looked like.
    # It helped me figure out the ranges below.    
    # Build a relationship between the two lists
    # Turn that relationship into a dictionary
    my_zip_alphabet = zip(alphabet, ord_alpha)
    dict_alphabet = dict(my_zip_alphabet)
    print(dict_alphabet)
    '''
    
    # 97 to 122 are lowercase
    # 65 to 90 are uppercase
    # Here are my indexes based on whether or not they are lowercase
    lowercase_idx = [x for x in range(97, 123)]
    uppercase_idx = [x for x in range(65,91)]
    
    result_text = ""
    for c in text:
        # Check for lowercase
        if (ord(c) <= max(lowercase_idx)) and (ord(c) >= min(lowercase_idx)):
            # Check for encrypt or decrypt
            if encrypt == True:
                # Find the index of the character based on its value so for example a = 97 would be at index 0
                # Shift the index by the shift amount
                # there are 26 letters in the alphabet so modulus 26 ensures we are not out of bounds on our list
                # find the value at the new index
                # Turn it back into a character and add it to my string
                result_text += chr(lowercase_idx[(lowercase_idx.index(ord(c)) + shift)%26])
            if encrypt == False:
                result_text += chr(lowercase_idx[(lowercase_idx.index(ord(c)) - shift)%26])
        # It is uppercase
        else:
            if encrypt == True:
                result_text += chr(uppercase_idx[(uppercase_idx.index(ord(c)) + shift)%26])
            if encrypt == False:
                result_text += chr(uppercase_idx[(uppercase_idx.index(ord(c)) - shift)%26])            
    
    print(result_text)

# Program starts here

keep_going = True
while keep_going:

    # Ensure only alphanumeric text is written
    non_alpha_text = True
    while non_alpha_text:
        text = input("Enter Cypher text: ")
        if text.isalpha():
            non_alpha_text = False


    # The user can choose to either encrypt or decrypt the message.
    # I turned this into a boolean value.
    bad_user_input = True
    while bad_user_input:
        user_encrypt = input("Type 'E' to Encrypt the message, or 'D' to Decrypt the message: ").lower()
        if user_encrypt == "e":
            encrypt = True
            bad_user_input = False
        elif user_encrypt == "d":
            encrypt = False
            bad_user_input = False

    # If they choose a number greater than 26 I want to catch it so I used a modulus
    # I am also not allowing negative numbers so I used the absolute value
    shift = abs(int(input("Type the shift number: "))%26)

    encrypt_decrypt(text=text, encrypt=encrypt, shift=shift)

    # Check to see if the user wants to continue.
    user_bad_input = True
    while user_bad_input:
        user_keep_going = input("Should we continue encoding or decoding? (Y or N)").lower()
        if user_keep_going == "y":
            keep_going = True
            user_bad_input = False
        elif user_keep_going == "n":
            keep_going = False
            user_bad_input = False
            print("Good bye!")


