"""
1. The onlyOneRightAnswer function takes 2 inputs a question which is given in the format of string and correct answer, there is a while loop defined in the function which will be executed once the function is called, it checks whether given input question and correct answer equal or not, if they are not equal it prints a statement.

2. The notAFactorial(9) loop executes infinitely.

3. To make the notAFactorial properly produce factorial, change the total to 1, in the code the total is assigned to 0, which will give value 0 for total value, and change the condition in while loop from num==num (which goes into infinite loop) to num>0.

4. I can add while True: condition to create an infinite loop.

5. It runs indefinitely.
"""


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
    if num<32:
        return "ask again later"
    elif(num==41):
        return "all signs point to yes"
    elif(num > 32 and num<=72):
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


if __name__ == "__main__":
    main()
