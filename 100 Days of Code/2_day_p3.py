'''
## Your Life in Weeks

# Instructions

I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

[https://waitbutwhy.com/2014/05/life-weeks.html](https://waitbutwhy.com/2014/05/life-weeks.html)

Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old. 

It will take your current age as the input and output a message with our time left in this format:

> You have x days, y weeks, and z months left. 

Where x, y and z are replaced with the actual calculated numbers. 

 

**Warning** your output should match the Example Output format exactly, even the positions of the commas and full stops. 

# Example Input

```
56
```

# Example Output

```
You have 12410 days, 1768 weeks, and 408 months left.
```

e.g. When you hit **run**, this is what should happen:  

 
![](https://cdn.fs.teachablecdn.com/RjqBViZQpyVTv7XY6cfA)
 

# Hint

1. There are 365 days in a year, 52 weeks in a year and 12 months in a year.
2. Try copying the example output into your code and replace the relevant parts so that the sentence is formated the same way.

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[https://repl.it/@appbrewery/day-2-3-test-your-code](https://repl.it/@appbrewery/day-2-3-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 


# Solution

[https://repl.it/@appbrewery/day-2-3-solution](https://repl.it/@appbrewery/day-2-3-solution)

'''

# They gave a hint
# 1. There are 365 days in a year, 52 weeks in a year and 12 months in a year.
# 2. Try copying the example output into your code and replace the relevant parts so that the sentence is formated the same way.

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Assumption is that we live till 90 years.
death_years = 90
death_months = 90*12
death_weeks = 90*52
death_days = 90*365

current_year = float(age)

current_months = current_year*12
current_weeks = current_year*52
current_days = current_year*365

years_left = int(death_years - current_year)
months_left = int(death_months - current_months)
weeks_left = int(death_weeks - current_weeks)
days_left = int(death_days-current_days)

print(f"You have {years_left} years left to live.\nYou have {months_left} months left to live.\nYou have {weeks_left} weeks left to live.\nYou have {days_left} days left to live.\n")