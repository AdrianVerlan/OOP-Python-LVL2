class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return f"[{self.value}]-- next --> {self.next}"
    
#Manual
head = Node(100)
print(head)
head.next = Node(200)
print(head)
head.next.next = Node(300)
print(head)
head.next.next.next = Node(400)
print(head)
head.next.next.next.next = Node(500)
print(head)
print()

# Automat using for loop
head = Node(100)
current_node = head

for value in [200, 300, 400, 500]:
    new_node = Node(value)
    current_node.next = new_node
    current_node = new_node

current_node = head
while current_node:
    print(current_node)
    current_node = current_node.next
