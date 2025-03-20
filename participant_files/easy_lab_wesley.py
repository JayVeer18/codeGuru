# input: question–a string with a prompting question, correctAnswer–the correct input
# output: asks the user to try again if answer was incorrect or moves on if correct
# Question 1: onlyOneRightAnswer ensures that the answer that is provided by the program is equal to the correct answer
# Question 2: notAFactorial will loop 10 times
# Question 3: First, it is multiplying the entire factorial by 0 every time because it is breaking when n < 0 not n = 0.
# '''' Second, it is doing the operation backwards, where it should be multiplying from 1 to n instead of from n to 1
# Question 4: We could answer anything other than n when prompted, which would cause the method to loop endlessly.
# Question 5: It runs until num < 0, so it will run N + 1 times.
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
    if num < 23:
        print("ask again later")
    if num == 43:
        print("all signs point to yes")
    if num <= 72:
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
