'''
1. onlyOneRightAnswer works by checking the contents of each of the strings and if they are not the same then an "error" message is 
shown to the user and if they are the sme then nothing happens to indicate the answer given and the expected answer are the same.

2. notAFactorial will execute 11 times but it should execute only 10 times.

3. The two things wrong are that the total should not be initialized to 0 because 0 times any number is 0 therefore it will always be 0 
and the second issue is that the while loop will almost always execute. It should instead check for a condition that can eventually become 
false to break the looping such as num >= 0.

4. We could change the loop condition to while True: which would result in an infinite loop, or we could do something ridiculous like while "hello" = "hello". We could 
also store the input in a variable before we enter the while loop and then check if that input is equal to itself which should always be true. We could do 
something else like while 1 > 0. Basically, there are infinite ways of doing this.

5. It will run forever because the logic inside of the loop is what updates num and also in the loop there is a break statement that will execute 
if num reaches a certain point (less than 0).
'''

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
'''
Write magic8(num) so that it uses num to predict an outcome. It must follow the following rules and return the appropriate strings

If num is less than 23, return "ask again later"
If num is 41, return "all signs point to yes"
If num is less than or equal to 72, return "outlook not so good"
Otherwise, return "concentrate and ask again"

For example, if someone calls the function with

magic8(-4) # the function would return "ask again later"
magic8(70) # the function would return "outlook not so good"

The function itself will not print or take in input from the client! Remember that when we want to write out a whole message, we usually use strings.
'''
def magic8(num):
    if (num < 23):
        return "ask again later"
    if (num == 41):
        return "all signs points to yes"
    if ((num <= 71) and (num != 41) and (num >= 23)):
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
