
"""
## Prime Numbers

# Instructions

Prime numbers are numbers that can only be cleanly divided by itself and 1. 

[https://en.wikipedia.org/wiki/Prime_number](https://en.wikipedia.org/wiki/Prime_number)


**You need to write a function** that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

 
 ![](https://cdn.fs.teachablecdn.com/s0gceS97QD6MP5RUT49H)

Here are the numbers up to 100, prime numbers are highlighted in yellow:

![](https://cdn.fs.teachablecdn.com/NZqVclSt2qAe8KhTsUtw)

# Example Input 1

```
73
```

# Example Output 1

```
It's a prime number.
```

# Example Input 2

```
75
```

# Example Output 2

```
It's not a prime number.
```

# Hint

1. Remember the modulus: 

[https://stackoverflow.com/questions/4432208/what-is-the-result-of-in-python](https://stackoverflow.com/questions/4432208/what-is-the-result-of-in-python)

2. Make sure you name your function/parameters the same as when it's called on the last line of code. 

3. Use the same wording as the Example Outputs to make sure the tests pass. 

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[https://repl.it/@appbrewery/day-8-2-test-your-code](https://repl.it/@appbrewery/day-8-2-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 


# Solution

[https://repl.it/@appbrewery/day-8-2-solution](https://repl.it/@appbrewery/day-8-2-solution)


"""


#Write your code below this line 👇

def prime_checker(number):
    # Recall Range does not include the last number, we also dont want to divide by 1
    range_of_numbers = range(2, number)

    # Return a list of the numbers that divide our number with no remainder. 
    prime_found = [n for n in range_of_numbers if number%n == 0]
    
    # If we found no numbers we know our number is prime.
    if set(prime_found) == ():
        print(f"{number} is a prime number.")
    else:
        # If we found numbers return them to the user. 
        # Set is most likely overkill since we are returning unique numbers. 
        # I used it above because in math we would have had an empty set. 
        # I could have also used []
        print(f"{number} is not prime it is divisable by {set(prime_found)}")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
