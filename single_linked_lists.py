class Node:
    def _init_(self, data):
        self.data = data
        self.next = None
        

node1 = Node(12)
node2 = Node(9)
node3 = Node(18)
node4 = Node(3)
node5 = Node(8)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


# Find the lowest value of data on the list
def findLowestValue(head):
    minValue = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    return minValue


# Function for printing the list traversing forward
def forward_traversal():
    currentNode = node1
    while currentNode:
        print(currentNode.data, "\n")
        currentNode = currentNode.next
    print("null")


def deleteNode(node1, nodeToDelete):
    if node1 == nodeToDelete:
        return node1.next

    currentNode = node1
    while currentNode.next and currentNode.next != nodeToDelete:
        currentNode = currentNode.next

    if currentNode.next is None:
        return node1

    currentNode.next = currentNode.next.next

    return node1


# Inserting a value to the list
def insert_end(data):
    new_node = Node(data)
    current = node1
    while current.next:
        current = current.next
    current.next = new_node


# Deleting data from list
def delete(data):
    global node1  # in case the head is deleted
    current = node1
    prev = None
    while current:
        if current.data == data:
            if prev:
                prev.next = current.next
            else:
                node1 = current.next  # deleting head
            return True  # data found and deleted
        prev = current
        current = current.next
    return False  # data not found



# Perform operation and print new list
delete(18)
print("\nAfter Deleting 18:")
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
pos = search(8)
print(f"\nPosition of 8: {pos}")


# Find the lowest value of data on the list
def findLowestValue(head):
    minValue = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    return minValue


# Perform operation and print new list
insert_end(19)
print("\nAfter Inserting 19:")
forward_traversal()

print("\n The lowest value in the linked list is:", findLowestValue(node1))
deleteNode(node1, node3)