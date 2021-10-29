'''
## Heads or Tails

# Instructions

You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails". 

**Important**, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

e.g.
1 means Heads
0 means Tails 

# Example Output

```
Heads
```

or

```
Tails
```


# Solution

[https://repl.it/@appbrewery/day-4-1-solution](https://repl.it/@appbrewery/day-4-1-solution)

'''

import random

heads_tails = random.randint(0,1)

if heads_tails == 0:
    print(f"You flipped a coin result is {0} Tails.")
elif heads_tails == 1:
    print(f"You flipped a coin result is {1} Heads.")
else:
    print("Random number generator created a number that is outside of what we were expecting.")