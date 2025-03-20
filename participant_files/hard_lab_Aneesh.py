# input: user input
# output: user input

#2 choco chipchoco Chip

#3 Base case is the if condition, if the list becomes empty then the
# recursion code breaks

#4 ["birthday cake", "strawberry, "maple"]
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
    ordersLength = len(orders)
    resultStr = ""
    if ordersLength == 0:
        return ""
    orderedList = separateOrders(orders[0])
    orderFlip = onePlateToAnother(orderedList)
    resultStr = "Order #{} your order of {} pancakes is up!".format(totalNum - ordersLength + 1, orderFlip)
    return resultStr + "\n" + orderUp(totalNum, orders[1:])


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
