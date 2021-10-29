'''
## Days in Month

# Instructions


In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function `is_leap()` so that instead of printing "Leap year." or "Not leap year." it should **return** `True` if it is a leap year and **return** `False` if it is not a leap year.

You are then going to create a function called `days_in_month()` which will take a **year** and a **month** as inputs, e.g.

```
days_in_month(year=2022, month=2)
```

And it will use this information to work out the **number of days in the month**, then **return** that as the **output**, **e.g.:**

```
28
```

The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.

# Hint

1. Look at the function call at the bottom of the code to see the positional arguments.  The order is very important.

2. Feel free to choose your own parameter names.

3. Remember that `month_days` is a List and Lists in Python start at position 0. So the number of days in January is `month_days[0]`

4. Be careful with indentation.

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[https://repl.it/@appbrewery/day-10-1-test-your-code](https://repl.it/@appbrewery/day-10-1-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 



# Solution

[https://repl.it/@appbrewery/day-10-1-solution](https://repl.it/@appbrewery/day-10-1-solution)

'''


def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
    leap_year = is_leap(year)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12 or month < 1:
        return "Invalid Month"

    if leap_year:
        return leap_month_days[month -1]
    else:
        return month_days[month -1]
        
   
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)