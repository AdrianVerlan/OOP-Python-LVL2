from Node import Node
def traverse(node):
    if not isinstance(node, Node):
        raise TypeError("Node must be an instance of Node class")

    curent = node
    while curent is not None:
        print(curent.subject)
        if curent.nextYes is None and curent.nextNo is None:
            print("Reached end of the tree")
            print(curent.subject)
            return

        answer = input("yes/no ? >>> ")
        if answer == "yes" and curent.nextYes is not None:
            curent = curent.nextYes
        elif answer == "no" and curent.nextNo is not None:
            curent = curent.nextNo
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")