'''
p
'''
# input: question–a string with a prompting question, correctAnswer–the correct input
# output: asks the user to try again if answer was incorrect or moves on if correct
def onlyOneRightAnswer(question, correctAnswer):
    while (input(question) != correctAnswer):
        print("Hmm... let's try that again!\n")
        
# the fn onlyOneRightAnswer has 2 parameters the question and the correct answer
'the while loop checks for the right ans and exits the loops if not the statment'
"Hmm... let's try that again! printd until the correct ans is given."

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
    
#ans2: the loop will run infinite times
#ans3 :The while (num == num) condition will always evaluate to True as long as num is a numeric value.
#This means that the loop will technically run indefinitely unless there is a break condition that stops it.
#You have an if statement inside the loop that checks if num < 0 and breaks out of the loop if that condition is met. However, since num is always non-negative due to the earlier condition (if num < 0), 
#this break condition won't be reached while num is positive

#Fixing the Function:
# def notAFactorial(num):  # there are 2 things wrong with this--how do we fix it to make it return the factorial?
#     total = 1
#     if num = 0:
#         num = num * (-1)
#     while (num >!0 ):
#         if num < 0:
#             break
#         else:
#             total = total * num
#             num = --num
#     return total

# input: none
# output: prints the factorials of numbers given to it

#ans4 
def askForInput():
    while True:
        num = int(input("Give me a number! \n"))
        fact = notAFactorial(num)
        print("The factorial of " + str(num) + " is " + str(fact))
    print("\nGoodbye!!")

# input: lucky number
# output: string with fortune
def magic8(num):
    if (num < 23):
        return ("ask again later")
    elif (num == 41):
        return ("all signs point to yes")
    elif ( num <=72):
        return ("outlook not so good")
    else:
        return ("concentrate and ask again")


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
