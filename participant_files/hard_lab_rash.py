#2. choco chip, strawberry, blueberry
#3. there are no pancakes left to be flipped
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
    temp2 = pancakes
    if(len(temp2) == 0):
        return []
    tempList = [temp2.pop(-1)] + onePlateToAnother(temp2)
    return tempList
    
def orderUp(totalNum, orders):
    # your code here!
    if(totalNum <= 0):
        return
    temporder = orders
    
    singleOrder = temporder.pop(totalNum-1).split(", ")
    orderUp(totalNum-1,temporder)
    singleOrder = onePlateToAnother(singleOrder)
    print("Order #" +str(totalNum) +", your order of "+ str(singleOrder) + " pancakes is up!")
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
