'''
## Average Height

# Instructions

You are going to write a program that calculates the average student height from a List of heights. 

e.g. `student_heights = [180, 124, 165, 173, 189, 169, 146]`

The average height can be calculated by adding all the heights together and dividing by the total number of heights. 

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = **1146**

There are a total of **7** heights in `student_heights`

1146 ÷ 7 = **163.71428571428572**

Average height rounded to the nearest whole number = **164**

**Important** You should not use the `sum()` or `len()` functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

# Example Input 

```
156 178 165 171 187
```

In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]

# Example Output 

```
171
```

e.g. When you hit **run**, this is what should happen: 

 
![](https://cdn.fs.teachablecdn.com/Nzb8hUVsQJ6STAGnvDCP)
 

# Hint

1. Remember to use the `round()` function to round the average height before you print it.

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[https://repl.it/@appbrewery/day-5-1-test-your-code](https://repl.it/@appbrewery/day-5-1-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 

# Solution

[https://repl.it/@appbrewery/day-5-1-solution](https://repl.it/@appbrewery/day-5-1-solution)
'''

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

print(type(student_heights))

# Quick option for averaging
ave = round(sum(student_heights)/len(student_heights))
print(ave)

# most likely how she expects us to do it
long_way_heights = 0
for i, v in enumerate(student_heights):
    long_way_heights += v

long_average = round(long_way_heights/(i+1))
print(long_average)