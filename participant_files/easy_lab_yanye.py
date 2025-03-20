'''
How does onlyOneRightAnswer work?
it prompts the user a question from the terminaal and then if the user doesn't enter the correctAnswer then the user is asked again.
This happens until the user answers correctly

How many times does notAFactorial(9) loop as it is currently written?
10 times

There are two things wrong with notAFactorial. What should we change about it to make it properly produce a factorial?
if num < 0 is wrong since then the total gets multiplied by 0 which causes the final answer to alwaays be 0
total should not start with 0 since anything multiplied by 0 is 0. It should be 1

How could we edit askForInput() to make it loop forever? (there are multiple correct answers)
while(true)

How long does the actual while loop for notAFactorial run, when ignoring what happens inside of it? (how long does while(num == num) run?
infinitely

'''




# input: question–a string with a prompting question, correctAnswer–the correct input
# output: asks the user to try again if answer was incorrect or moves on if correct
def onlyOneRightAnswer(question, correctAnswer):
    while (input(question) != correctAnswer):
        print("Hmm... let's try that again!\n")


# input: num–an int of some kind
# output: the positive factorial of num
def notAFactorial(num):  # there are 2 things wrong with this--how do we fix it to make it return the factorial?
    total = 1
    if num < 0:
        num = num * (-1)
    while (num == num):
        if num <= 0:
            break
        else:
            total = total * num
            num = num - 1
    return total


# input: none
# output: prints the factorials of numbers given to it
def askForInput():
    while (input("Would you like to go again? y/n \n") != "n"):
        num = int(input("Give me a number! \n"))
        fact = notAFactorial(num)
        print("The factorial of " + str(num) + " is " + str(fact))
    print("\nGoodbye!!")


# input: lucky number
# output: string with fortune
def magic8(num):
    if (num < 23):
        return "ask again later"
    if (num == 41):
        return "all signs point to yes"
    if (num <= 72):
        return "outlook not so good"
    return "concentrate and ask again"


def main():
    ''' This Streamlit code editor has limited functionality, user cannot give input. Hence commenting these'''
    # askForInput()
    # onlyOneRightAnswer("Would you like your fortune read?y/n\n ", "y")
    # fortuneNum = int(input("Great! Give me your luckiest number from 0-100!\n"))
    # magic8(fortuneNum)  # you will write this one!

    '''Testing your program. If you get the expected output, your lab is done'''
    print("TESTING", magic8(-4))
    print("TESTING", magic8(70))
    
    print(notAFactorial(5))
    print(notAFactorial(0))


if __name__ == "__main__":
    main()
