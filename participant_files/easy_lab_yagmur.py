#onlyOneRightAnswer takes two parameters; a question and a correct answer. 
#If the answer to the question doesn't match the correct answer, the program prints "Hmm... Let's try that again."
#notAFactorial turns into an infinite loop since we turn the negative values into positive ones before the while loop.
#the total should be initialized as 1, not 0.
#the while loop should only continue when num is not equal to 0.
#to make askForInput() loop forever, we could not check if the answer is yes or no, the program could keep asking until forever.
#the while(num = num) runs infinitely since num will always be equal to itself.
# input: question–a string with a prompting question, correctAnswer–the correct input
# output: asks the user to try again if answer was incorrect or moves on if correct
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
    # student code
    if num < 23:
        return "ask again later"
    if num == 41:
        return "all signs point to yes"
    if num <= 71:
        return "outlook not so good"
    else:
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
    print("TESTING", magic8(41))


if __name__ == "__main__":
    main()
