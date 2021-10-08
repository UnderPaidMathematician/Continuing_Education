
'''
## Pizza Order

# Instructions

Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program. 

Based on a user's order, work out their final bill. 

```
Small Pizza: $15
```

```
Medium Pizza: $20
```

```
Large Pizza: $25
```

```
Pepperoni for Small Pizza: +$2
```

```
Pepperoni for Medium or Large Pizza: +$3
```

```
Extra cheese for any size pizza: + $1
```

# Example Input

```
size = "L"
```

```
add_pepperoni = "Y"
```

```
extra_cheese = "N"
```

# Example Output

```
Your final bill is: $28.
```

e.g. When you hit **run**, this is what should happen:  

 
![](https://cdn.fs.teachablecdn.com/p1evEkwQxGNR4WlolIb4)
  

# Hint

1. Think about what you've learnt about multiple if statements and see if you can reduce the number of lines of code while having the same functionality.

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[https://repl.it/@appbrewery/day-3-4-test-your-code](https://repl.it/@appbrewery/day-3-4-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 



# Solution

[https://repl.it/@appbrewery/day-3-4-solution](https://repl.it/@appbrewery/day-3-4-solution)

'''

# Their example offered no real input error checking. 
# I decided to add some while loops to check user inputs.

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Check customer inputs
# Lets assume that they made a mistake
size_input_failure = True

list_size = ["s", "m", "l"]
list_pepperoni = ["y", "n"]
list_extra_cheese = ["y", "n"]

total_bill = 0

while size_input_failure:
    for s in list_size:
        if (s == size.lower()) and (s == "s"):
            total_bill += 15
            size_input_failure = False
        elif (s == size.lower()) and (s == 'm'):
            total_bill += 20
            size_input_failure = False
        elif (s == size.lower()) and (s == 'l'):
            total_bill += 25
            size_input_failure = False

    if size_input_failure == True:
        print("Invalid input")
        size = input("What size pizza do you want? S, M, or L ")

pepperoni_input_failure = True

while pepperoni_input_failure:
    for p in list_pepperoni:
        if (p == add_pepperoni.lower()) and (p == 'y') and (size.lower() == "s"):
            total_bill += 2
            pepperoni_input_failure = False
        elif (p == add_pepperoni.lower()) and (p == 'y') and (size.lower() != "s"):
            total_bill += 3
            pepperoni_input_failure = False

        elif (p == add_pepperoni.lower()) and (p == 'n'):
            pepperoni_input_failure = False
    
    if pepperoni_input_failure == True:
        print("Invalid input")
        add_pepperoni = input("Do you want pepperoni? Y or N ")

extra_cheese_input_failure = True

while extra_cheese_input_failure:
    for c in list_extra_cheese:
        if (c == extra_cheese.lower()) and (c == 'y'):
            total_bill += 1
            extra_cheese_input_failure = False
        elif (c == extra_cheese.lower()) and (c == 'n'):
            extra_cheese_input_failure = False
    
    if extra_cheese_input_failure == True:
        print("Invalid input")
        extra_cheese = input("Do you want extra cheese? Y or N ")

print(total_bill)

            
        


