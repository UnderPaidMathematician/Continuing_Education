'''
## Who's Paying

# Instructions

You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill. 

**Important**: You are not allowed to use the `choice()` function.

**Line 8** splits the string `names_string` into individual names and puts them inside a **List** called `names`. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

# Example Input

```
Angela, Ben, Jenny, Michael, Chloe
```
Note: notice that there is a space between the comma and the next name. 
# Example Output

```
Michael is going to buy the meal today!
```


# Hint

1. You might need the help of the `len()` function.   

[https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list](https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list)

2. Remember that Lists start at index 0!

# Solution

[https://repl.it/@appbrewery/day-4-2-solution](https://repl.it/@appbrewery/day-4-2-solution)
'''

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

# since we are starting at 0 we need to remove one from the length of the list 
who_pays = random.randint(0, len(names)-1)

# showing the members of the list 
print("Today the following people put their credit card in the bowl.\n")
for n in names:
    print(n)
    
print(f"\nToday {names[who_pays]} will pay the bill.")
