'''
## Variables

# Instructions

Write a program that switches the values stored in the variables a and b. 

**Warning.** Do not change the code on lines 1-4 and 12-18. Your program should work for different inputs. e.g. any value of a and b.

# Example Input

```
a: 3
```

```
b: 5
```

# Example Output

```
a: 5
```

```
b: 3
```

e.g. When you hit **run**, this is what should happen:

![](https://cdn.fs.teachablecdn.com/tgdNl0iSqK6RpPyYZh9d)

# Hint

1. You should not have to type any numbers in your code. 
2. You might need to make some more variables.

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[https://repl.it/@appbrewery/day-1-4-test-your-code](https://repl.it/@appbrewery/day-1-4-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 




# Solution

[https://repl.it/@appbrewery/day-1-4-solution](https://repl.it/@appbrewery/day-1-4-solution)
'''

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# Storing my values in a list
temp_list = []
temp_list.append(a)
temp_list.append(b)

# Playing with indexes I could have called 1 and 0 here also
a=temp_list[-1]
b=temp_list[-2]


#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)