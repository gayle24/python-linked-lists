class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

node1 = Node(500)
node2 = Node(37)
node3 = Node(78)
node4 = Node(128)

node1.next = node2
node1.prev = node4

node2.next = node3
node2.prev = node1

node3.next = node4
node3.prev = node2

node4.next = node1
node4.prev = node3

print("\n Traversing Forward")
currentNode = node1
startNode = node1
print( currentNode.data, end="-> ")
currentNode = currentNode.next

while currentNode != startNode:
    print( currentNode.data, end="-> ")
    currentNode = currentNode.next

print("\n Traversing Backward")
currentNode = node4
startNode = node4
print( currentNode.data, end="-> ")
currentNode = currentNode.prev

while currentNode != startNode:
    print( currentNode.data, end="-> ")
    currentNode = currentNode.prev