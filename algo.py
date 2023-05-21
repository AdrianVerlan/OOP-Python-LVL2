from Node import Node
def traverse (node):
    if not isinstance(node,Node):
        raise TypeError("Node must be an insistance of Node class")
    if node.nextYes is None and node.nextNo is None:
        print("Reached end of the tree")
        print(node.subject)
        return
    
    print(node.subject)
    answer = input("yes/no ? >>> ")

    if answer =="yes" and node.nextYes is not None:
        traverse(node.nextYes)
    if answer == "no" and node.nextNo is not None:
        traverse(node.nextNo)
    
