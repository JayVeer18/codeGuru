"""
1. How does onlyOneRightAnswer work?

Considering user gives 'y' it exists.
if user gives 'n', while loop prints "Hmm... let's try that again!
"""

# input: question–a string with a prompting question, correctAnswer–the correct input
# output: asks the user to try again if answer was incorrect or moves on if correct
def onlyOneRightAnswer(question, correctAnswer):
    while (input(question) != correctAnswer):
        print("Hmm... let's try that again!\n")


"""
How many times does notAFactorial(9) loop as it is currently written?
ans: 9 times

"""
# input: num–an int of some kind
# output: the positive factorial of num
def notAFactorial(num):  # there are 2 things wrong with this--how do we fix it to make it return the factorial?
    total = 0
    if num < 0:
        num = num * (-1)
    while (num == num):
        if num < 0:
            break
        else:
            total = total * num
            num = num - 1
    return total


"""
3. There are two things wrong with notAFactorial. What should we change about it to make it properly produce a factorial?

total should be 1
"""
# input: none
# output: prints the factorials of numbers given to it
def askForInput():
    while (input("Would you like to go again? y/n \n") != "n"):
        num = int(input("Give me a number! \n"))
        fact = notAFactorial(num)
        print("The factorial of " + str(num) + " is " + str(fact))
    print("\nGoodbye!!")

"""
How could we edit askForInput() to make it loop forever? (there are multiple correct answers)

using while TRUE 
"""
# input: lucky number
# output: string with fortune
def magic8(num):
    if num < 23:
        return "ask again later"
    elif num == 41:
        return "all signs point to yes"
    elif num <= 72:
        return "outlook not so good"
    else:
        return "concentrate and ask again"

"""
How long does the actual while loop for notAFactorial run, when ignoring what happens inside of it? (how long does while(num == num) run?

Loop will run indefinitely as (num== num)
"""
def main():
    ''' This Streamlit code editor has limited functionality, user cannot give input. Hence commenting these'''
    # askForInput()
    # onlyOneRightAnswer("Would you like your fortune read?y/n\n ", "y")
    # fortuneNum = int(input("Great! Give me your luckiest number from 0-100!\n"))
    # magic8(fortuneNum)  # you will write this one!

   
    '''Testing your program. If you get the expected output, your lab is done'''
    print("TESTING", magic8(-4))
    print("TESTING", magic8(70))


if __name__ == "__main__":
    main()
