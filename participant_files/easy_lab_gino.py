# input: question–a string with a prompting question, correctAnswer–the correct input
# output: asks the user to try again if answer was incorrect or moves on if correct
# 1.) It looks like it keeps going through until they correctly guess the answer right!
# 2.) 1 time, as the else statement will times 9 with 0 then end.
# 3.) Change the total to something else from 0 and change num = num * (-1)
# 4.) Making the while loop true, meaning if the askForInput() is true, it will run indefinitly!
# 5.) Since the num is - 1, it will keep running till its -1, or loop 9 times.
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



# input: lucky number
# output: string with fortune
def magic8(num):
    if (num < 23):
        print("ask again later")
    elif (num == 41):
        print("all signs point to yes")
    elif (num <= 72):
        print("outlook not so good")
    else:
        return("concentrate and ask again")


def main():
    ''' This Streamlit code editor has limited functionality, user cannot give input. Hence commenting these'''
    #askForInput()
    # onlyOneRightAnswer("Would you like your fortune read?y/n\n ", "y")
    # fortuneNum = int(input("Great! Give me your luckiest number from 0-100!\n"))
    # magic8(fortuneNum)  # you will write this one!

    '''Testing your program. If you get the expected output, your lab is done'''
    print("TESTING", magic8(-4))
    print("TESTING", magic8(70))
    print("TESTING", magic8(41))
    print("TESTING", magic8(100))
    print("TESTING", notAFactorial(9))


if __name__ == "__main__":
    main()
