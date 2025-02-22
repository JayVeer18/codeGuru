# Lab: TryAgain
This lab contains question related to  Loops and if statements

# Attached is some code
Review the code provided. Answer the following questions by adding comments to your code! You are free to talk with other students and seek better understanding to these questions. See below for reminders on types, variables, and input

# Step One
Complete the following questions in the comments at the top of your code. If your answer is multiple lines, use these: \``` around your answer:
1. How does onlyOneRightAnswer work?
2. How many times does notAFactorial(9) loop as it is currently written?
3. There are two things wrong with notAFactorial. What should we change about it to make it properly produce a factorial?
4. How could we edit askForInput() to make it loop forever? (there are multiple correct answers)
5. How long does the actual while loop for notAFactorial run, when ignoring what happens inside of it? (how long does while(num == num) run?


# Step Two: Coding: magic8(num)
Find the function `magic8(num)`. 

Write magic8(num) so that it uses num to predict an outcome. It must follow the following rules and return the appropriate strings
```
If num is less than 23, return "ask again later"
If num is 41, return "all signs point to yes"
If num is less than or equal to 72, return "outlook not so good"
Otherwise, return "concentrate and ask again"
```

For example, if someone calls the function with
```python
magic8(-4) # the function would return "ask again later"
magic8(70) # the function would return "outlook not so good"
```
The function itself will not print or take in input from the client! Remember that when we want to write out a whole message, we usually use strings.

# Step Three: Test magic8(num)
How do you test code? You simply add the lines to your python file (in the future, you will have test lines in separate files).

As such, we would recommend adding the following just above def main().
```python
print("TESTING", magic8(-4))
print("TESTING", magic8(70))
```
Also add your own tests!

# Submitting the Assignment
Make sure you run the code with no errors and then save the code. The Co-Investigators will then evaluate your code against the zybooks to get the final score once the experiment is done.

# Reminder on if statements
When writing if statements, you want to start with your most specific checks first. For example, if you have code that checks if x == 1 and also checks if x < 2, you want to check x == 1 **first**. If you check it AFTER you check x < 2, it will never be seen because 1 < 2. This also works with ranges, for example, checking the numbers less than 25, and checking the numbers between 25 and 100, because by the time we get to 25 <= x <= 100, we already know that 25 <= x, because x is **not** < 25.

# Reminder on loops
While loops are basically just if statements that are checked until they don't meet the if statement condition anymore. Because of this, if we have a condition that never changes, the while loop will loop infinately. On the opposite end, if we have a condition that **starts** false, we never go into the while loop at all. 
Unchanging conditions that are infinite: n == n, True
Unchanging conditions that start false: 1 == 0, False
