'''
Take a look at the flow diagram below. This is the flow diagram for separateOrders(str). On a piece of paper, or something separate, make a flow diagram for onePlateToAnother() and show it to a TA when you're done.
What is the output for onePlateToAnother([“blueberry”, “strawberry”, “choco chip”]?
['choco chip', 'strawberry', 'blueberry']

What is the base case for onePlateToAnother(pancakes)?
if the length of pancakes is 0, so the list is empty

What is the output for main() when this is the input?: maple Y strawberry y birthday cake n double chocolate


'''




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
    if (len(orders) == 0):
        return 
    else:
        # pancakes = onePlateToAnother(orders)
        # print(pancakes)
        #print(separateOrders(pancakes))
        # print("Order #" + str((totalNum-len(orders))+1) + ", your order of [" + ", ".join([str(item) for item in orders]) + "] is up!")
        return orderUp(totalNum, orders[1:])


# What is this function doing?
def main():
    ''' This Streamlit code editor has limited functionality, user cannot give input. Hence commenting these'''
    pancakeStack = [takeOrders()]
    while (input("Would you like anything else? y/n\n").lower() != "n"):
        pancakeStack.append(takeOrders())
    madeOrder = onePlateToAnother(pancakeStack)
    print("Your order of {} is up!".format(madeOrder))
    # print("TESTING",
          # orderUp(3, ["blueberry, strawberry", "plain, whole wheat", "banana nut, birthday cake, chocolate chip"]))
    print(onePlateToAnother(["blueberry", "strawberry", "choco chip"]))

if __name__ == "__main__":
    main()
