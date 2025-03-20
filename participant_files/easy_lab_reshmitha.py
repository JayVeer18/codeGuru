# input: question–a string with a prompting question, correctAnswer–the correct input
# output: asks the user to try again if answer was incorrect or moves on if correct
'''1-onlyOneRightAnswer accepts two parameters and it prompts the user for question and compares the answer entered by user with the correct answer.
If it's not a match, then it prints the error message
2- notAFactorial - the loop runs for 11 times. 
3- It should have been num<=0 inside the loop at if.total should have been initialized to 1 instead of 0.
4- Remove break statement, Remove the decrement of num in else statement
5-Infinitely'''
def onlyOneRightAnswer(question, correctAnswer):
    while (input(question) != correctAnswer):
        print("Hmm... let's try that again!\n")


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
    output=''
    '''If num is less than 23, return "ask again later"
If num is 41, return "all signs point to yes"
If num is less than or equal to 72, return "outlook not so good"
Otherwise, return "concentrate and ask again"'''
    if num<23:
        output = 'ask again later'
    elif num==41:
        output =  'all signs point to yes'
    elif num<=72:
        output =  'outlook not so good'
    else:
        output = 'concentrate and ask again' 
    # student code
    return output


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
