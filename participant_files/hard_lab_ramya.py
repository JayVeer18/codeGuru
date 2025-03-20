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
# output: ['choco chip', 'strawberry', 'blueberry']
# 'ans 3 : The base case for the function onePlateToAnother(pancakes) is when the list pancakes is empty:

# if len(pancakes) == 0:
#     return []'

# 'ans 3 :['maple', 'strawberry']'
def onePlateToAnother(pancakes):
    if (len(pancakes) == 0):
        return []
    else:
        return [pancakes[len(pancakes) - 1]] + onePlateToAnother(pancakes[:len(pancakes) - 1])

def orderUp(totalNum, orders):
    # Helper function to separate a string of pancake orders into a list
def separateOrders(str):
    if (str.find(",") == -1):
        return [str]
    return [str[: str.find(",")]] + separateOrders(str[str.find(",") + 2:])

# Helper function to reverse the list of pancakes (simulating onePlateToAnother behavior)
def onePlateToAnother(pancakes):
    if len(pancakes) == 0:
        return []
    else:
        return [pancakes[len(pancakes) - 1]] + onePlateToAnother(pancakes[:len(pancakes) - 1])

# Main function to process all orders
def orderUp(totalNum, orders):
    # Base case: no more orders to process
    if len(orders) == 0:
        return
    
    # Process the first order
    order = orders[0]
    
    # Separate the pancakes into a list
    separated_order = separateOrders(order)
    
    # Reverse the order using onePlateToAnother
    reversed_order = onePlateToAnother(separated_order)
    
    # Calculate the order number based on remaining orders
    order_number = totalNum - len(orders) + 1
    
    # Output the formatted message
    print(f"Order #{order_number}, your order of {reversed_order} pancakes is up!")
    
    # Recursively call orderUp for the remaining orders
    orderUp(totalNum, orders[1:])

# Test the function
orderUp(3, ["blueberry, strawberry", "plain, whole wheat", "banana nut, birthday cake, chocolate chip"])
 


#step 3 :

ef separateOrders(str):
    if (str.find(",") == -1):
        return [str]
    return [str[: str.find(",")]] + separateOrders(str[str.find(",") + 2:])

# Helper function to reverse the list of pancakes (simulating onePlateToAnother behavior)
def onePlateToAnother(pancakes):
    if len(pancakes) == 0:
        return []
    else:
        return [pancakes[len(pancakes) - 1]] + onePlateToAnother(pancakes[:len(pancakes) - 1])

# Main function to process all orders
def orderUp(totalNum, orders):
    # Base case: no more orders to process
    if len(orders) == 0:
        return
    
    # Process the first order
    order = orders[0]
    
    # Separate the pancakes into a list
    separated_order = separateOrders(order)
    
    # Reverse the order using onePlateToAnother
    reversed_order = onePlateToAnother(separated_order)
    
    # Calculate the order number based on remaining orders
    order_number = totalNum - len(orders) + 1
    
    # Output the formatted message
    print(f"Order #{order_number}, your order of {reversed_order} pancakes is up!")
    
    # Recursively call orderUp for the remaining orders
    orderUp(totalNum, orders[1:])


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
