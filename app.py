from Node import Node
from algo import traverse

n1 = Node("1.Do you want to go to the Sea? ")
n1.nextYes = Node("2. Succes")
n1.nextNo = Node("3.Do you want to go to the Mountain? ")

n1.nextNo.nextYes = Node("4. Succces!")
n1.nextNo.nextNo = Node("5. Do you want to go to the pool? ")

n1.nextNo.nextNo.nextYes= Node("6.Succes!")
n1.nextNo.nextNo.nextNo= Node("7.Unsucces!")

#print(n1)
#traverse(12)
traverse(n1)
