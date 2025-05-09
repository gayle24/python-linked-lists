# double linked lists

# 1. Initialising the node class
class Node:
    # 2. Define function for the node to hold the data and the reference pointer
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Creating the nodes
node1 = Node(12)
node2 = Node(25)
node3 = Node(34)
node4 = Node(87)
node5 = Node(89)

# Creating pointers to the nodes (previous and next)
node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3

#Function for printing the list traversing forward
def forward_traversal():
    print("\nForward Traversal")
    currentNode = node1
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

#Function for printing the list traversing backward
print("\nBackward Traversal:")
currentNode = node4
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.prev
print("null")


# Find the lowest value of data on the list
def findLowestValue(head):
    minValue = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    return minValue

print("The lowest value in the linked list is:", findLowestValue(node1))


# Inserting a value to the list
def insert_end(data):
    new_node = Node(data)
    current = node1
    while current.next:
        current = current.next
    current.next = new_node
    new_node.prev = current


# Perform operation and print new list
insert_end(15)
print("\nAfter Inserting 15:")
forward_traversal()


# Deleting data from list
def delete(data):
    global node1  # in case the head is changed
    current = node1
    while current:
        if current.data == data:
            if current.prev:
                current.prev.next = current.next
            else:
                node1 = current.next  # deleting head

            if current.next:
                current.next.prev = current.prev
            return True  # data found and deleted
        current = current.next
    return False  # data not found

# Perform operation and print new list
delete(34)
print("\nAfter Deleting 34:")
forward_traversal()


# Sorting out data from the list
def sort():
    if node1 is None:
        return
    swapped = True
    while swapped:
        swapped = False
        current = node1
        while current.next:
            if current.data > current.next.data:
                current.data, current.next.data = current.next.data, current.data
                swapped = True
            current = current.next

# Perform operation and print new list
sort()
print("\nAfter Sorting:")
forward_traversal()


# Searching data from the list
def search(data):
    current = node1
    position = 0
    while current:
        if current.data == data:
            return position
        current = current.next
        position += 1
    return -1  # not found

# Perform operation and print new list
pos = search(87)
print(f"\nPosition of 87: {pos}")
