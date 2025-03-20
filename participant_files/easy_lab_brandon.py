"""
1.  onlyOneRightAnswer takes two inputs, a question and a correct answer.
    Then, it enters a while loop with the condition that question doesn'that
    equal the correct answer, printing "Hmm... let's try that again". 
    Once the input question matches the correct answer the while loop is ended.
    
2.  11 times if num = 9.

3.  The total gets returned as 0 when it should be returning the factorial product.
    Also if we do fix the total problem, due to it being = 0, at the beginning of the
    function, it will eventually be set back to 0 since the while loop
    runs when num == 0.
    
4. You could set the condition in askForInput to while(true) and never 
   change the value of true to false to have it loop forever.
   
5.  If nothing happens inside the while(num == num) loop it would run
    forever.
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
    # student code
    if num < 23:
        return "ask again later"
    if num == 41:
        return "all signs point to yes"
    if num <= 72:
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


if __name__ == "__main__":
    main()
