#1. onlyOneRightAnswer works by continously checking if you have input the correct answer, and if you haven't it outputs try again
#2. 10 times
#3. Set total = 1 at the start and break if num is equal to zero
#4. make it a while true loop that asks for input inside the loop
#5. it would run forever, as any variable is always equal to itself
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
    if(num < 23):
        print("ask again later")
    elif(num == 41):
        print("all signs point to yes")
    elif(num <= 72):
        print("outlook not so good")
    else:
        print("concentrate and ask again")
    return


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
