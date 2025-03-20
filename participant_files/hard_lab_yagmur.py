#the output for Q2 is choco chip , strawberry, and then blueberry.
#the base case for onePlateToAnother is len(pancakes) == 0
#the input in Q3 is not a list so it will not run.

# input: user input
# output: user input
def takeOrders():
    return input("What would you like today?\n")


# input: string of comma-separated types of pancakes
# output: list of types of pancakes
# ex: input: "rice, whole wheat, chocolate" output: [“rice”, “whole wheat”, “chocolate”]
def separateOrders(str):
    if (str.find(",") == -1):
        return [str]
    return [str[: str.find(",")]] + separateOrders(str[str.find(",") + 2:])


# input: pancakes–a list that contains a stack of pancakes
# output: you answer :)
def onePlateToAnother(pancakes):
    if (len(pancakes) == 0):
        return []
    else:
        return [pancakes[len(pancakes) - 1]] + onePlateToAnother(pancakes[:len(pancakes) - 1])


def orderUp(totalNum, orders):
    # your code here!
    orderNum = len(separateOrders(orders))
    
    return


# What is this function doing?
def main():
    ''' This Streamlit code editor has limited functionality, user cannot give input. Hence commenting these'''
    # pancakeStack = [takeOrders()]
    # while (input("Would you like anything else? y/n\n").lower() != "n"):
    #     pancakeStack.append(takeOrders())
    # madeOrder = onePlateToAnother(pancakeStack)
    # print("Your order of {} is up!".format(madeOrder))
    print("TESTING",
          orderUp(3, ["blueberry, strawberry", "plain, whole wheat", "banana nut, birthday cake, chocolate chip"]))


if __name__ == "__main__":
    main()
