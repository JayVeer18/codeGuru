"""
2. The output is ["cocochip",strawberry", "blueberry"]

3. The base code for the onePlateToAnother function is the if condition, if the pancakes are empty the function returns an empty list.

4. The ouput for the main function is ["birthday cake", "strawberry", "maple"]

"""

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
    if not orders:
        return
    else:
        separate_list = separateOrders(orders[0])
        reverse_pancakes = onePlateToAnother(separate_list)
        
        order_number = totalNum - len(orders) + 1
        
        print(f"Order #{order_number}, your order of {reverse_pancakes} pancakes is up!")
        
        orderUp(totalNum, orders[1:])


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
