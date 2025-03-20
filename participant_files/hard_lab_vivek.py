'''
2. strawberry, blueberry is the first order, chocochip is the second order.
3. Base case is that length of the pancakes should be greater than zero. 
4. Order #1, your order of ["maple", "strawberry", "chocolate cake"] is up.
Order #2, your order of ["double chocolate"] is up.
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
    order = []
    if len(orders) == 0:
        return order# Base case: no more orders to process

    # Step 1: Get the first order and separate it
    first_order = orders[0]
    separated_order = separateOrders(first_order)

    # Step 2: Reverse the pancakes
    reversed_order = onePlateToAnother(separated_order)

    # Step 3: Determine the order number
    order_number = totalNum - len(orders) + 1

    # Step 4: Print the order
    order.append(f"Order #{order_number}, your order of {reversed_order} pancakes is up!")

    # Step 5: Recursive call with the remaining orders
    return orderUp(totalNum, orders[1:])  # Call with the rest of the orders

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
