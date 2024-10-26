# Lab04OperationStation
Operations Warmup Lab

# Attached is some code
Review the code provided. Answer the following questions by adding comments to your code! You are free to talk with other students, and seek better understanding to these questions. See below for reminders on types, variables, and input

# Step One
Complete the following questions in the comments at the top of your code. If your answer is multiple lines, use these: \``` around your answer:
1. What is howManyEven() doing? What is the output for howManyEven(9)?
2. What does isOdd(3) return? Why?
3. Recall the factorial code from the previous lab. Rewrite the corrected factorial code using our new -=, +=, *=, /= (etc) operators.
4. How can we rewrite n = int(¾) using // to make the output look the same?

# Step Two -- Coding noChange(cents)
You are someone who hates carrying around loose change. 
Write `noChange(cents)` such that it takes in some amount of cents and rounds it to whole dollars, ignoring all remaining change. 
```
If it rounds evenly already, print “Hoorah!” before returning the whole dollars. 
If it does not, print “Keep the change!” before returning the whole dollars.
```

For example,
```python
noChange(100) # the output should print "Hoorah!" and return 1
noChange(225) # the output should print "Keep the change!" and return 2
```

# Step Three: Test noChange(cents)
How do you test code? You simply add the lines to your python file (in the future, you will have test lines in separate files).

As such, we would recommend adding the following just above def main().
```python
print("TESTING", noChange(100)) 
print("TESTING", noChange(225)) 
```
Also add your own tests!

# Submitting the Assignment
Make sure to submit the assignment for grading! If you haven't clicked through the canvas link in a while, we would suggest clicking through it again before submitting.

# Reminder on Combination Operations
Combination operations, or operations like += and -= are a combination of the math operation and the assignment operation. 
This means that x += 3 really means x = x + 3. These are essentially just short hand for when you're doing simple math to a variable and want that that to go back into the variable. If you want to have full control over your order of operations, I recommend using x = x + 3 instead, so that you can do things like x = (x + 3) * 4.

# Reminder on % (modulo) and //
% and // are sort of opposites. Both do division on the numbers to the left and right of them. 
However, % will get the remainder of that division (Ex. 7 % 3 = 1).
// gets the whole number of the divison, or the number on the left side of the decimal (Ex. 7 // 3 = 2).

