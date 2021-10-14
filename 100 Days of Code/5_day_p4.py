'''
## FizzBuzz

# Instructions

You are going to write a program that automatically prints the solution to the FizzBuzz game. 

> `Your program should print each number from 1 to 100 in turn.` 

>   `When the number is divisible by 3 then instead of printing the number it should print "Fizz".` 

>     `When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 

>       `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`

e.g. it might start off like this:

```
`1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz`
```

`.... etc.`

# Hint

1. Remember your answer should start from 1 and go up to and including 100. 

2. Each number/text should be printed on a separate line.

# Solution

[https://repl.it/@appbrewery/day-5-4-solution](https://repl.it/@appbrewery/day-5-4-solution)

Alternatively: [https://en.wikipedia.org/wiki/Fizz_buzz](https://en.wikipedia.org/wiki/Fizz_buzz)


'''

for number in range(1,101):
    
    options = {3:"Fizz", 5:"Buzz", 35:"FizzBuzz"}

    if (number % 3) == 0 and (number % 5) == 0:
        print(f"{number} is divisible by both 3 and 5: {options[35]}")
    elif (number % 3) == 0:
        print(f"{number} is divisible by 3: {options[3]}")
    elif (number % 5) == 0:
        print(f"{number} is divisible by 5: {options[5]}")
    else:
        print(f"{number} is neither divisible by 3 or 5. ")
        
print(
"""
If the number is divisible by 3 we get Fizz.
If the number is divisible by 5 we get Buzz.
If the number is divisible by both we get FizzBuzz.

""")
