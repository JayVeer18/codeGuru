# input: question–a string with a prompting question, correctAnswer–the correct input
# output: asks the user to try again if answer was incorrect or moves on if correct

''' 1) if we give the the input that is not equal to the correct answer, we will encounter the message "Hmm... let's try that again!" 
in a loop until the input and correct answer are equal.

2) 10 times

3) variable 'total' should be assigned to 1.
changing the while loop.

4) by changing the condition in the while loop.

5) until the number becomes negative.

'''


def onlyOneRightAnswer(question, correctAnswer):
    while (input(question) != correctAnswer):
        print("Hmm... let's try that again!\n")


# input: num–an int of some kind
# output: the positive factorial of num
def notAFactorial(num):  # there are 2 things wrong with this--how do we fix it to make it return the factorial?
    total = 1
    if num < 0:
        num = num * (-1)
    while (num > 0):
            total = total * num
            num = num - 1
    return total


# input: none
# output: prints the factorials of numbers given to it
def askForInput():
    while (input("Would you like to go again? y/n \n") == 1):
        num = int(input("Give me a number! \n"))
        fact = notAFactorial(num)
        print("The factorial of " + str(num) + " is " + str(fact))
    print("\nGoodbye!!")


# input: lucky number
# output: string with fortune
def magic8(num):
    # student code
    if num<23:
        return "ask again later"
    elif num==41:
        return ("all signs point to yes")
    elif num<=72:
        return ("outlook not so good")
    else:
        return ("concentrate and ask again")


def main():
    ''' This Streamlit code editor has limited functionality, user cannot give input. Hence commenting these'''
    # askForInput()
    # onlyOneRightAnswer("Would you like your fortune read?y/n\n ", "y")
    # fortuneNum = int(input("Great! Give me your luckiest number from 0-100!\n"))
    #magic8(fortuneNum)  # you will write this one!

    '''Testing your program. If you get the expected output, your lab is done'''
    print("TESTING", magic8(-4))
    print("TESTING", magic8(70))


if __name__ == "__main__":
    main()
