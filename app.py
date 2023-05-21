from Node import Node
from algo import traverse

n1 = Node("1.Solve it peaceful betwen the parts? ")
n1.nextYes = Node("2. Succes")
n1.nextNo = Node("3.Reported and solved by superior? ")

n1.nextNo.nextYes = Node("4. Succces!")
n1.nextNo.nextNo = Node("5. Solve by law? ")

n1.nextNo.nextNo.nextYes= Node("6.Succes!")
n1.nextNo.nextNo.nextNo= Node("7.Unsucces!")

#print(n1)
#traverse(12)
traverse(n1)
