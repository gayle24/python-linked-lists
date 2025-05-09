class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Point to itself
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def delete(self, key):
        if not self.head:
            return

        current = self.head
        prev = None

        while True:
            if current.data == key:
                if prev:
                    prev.next = current.next
                else:
                    # Deleting head node
                    tail = self.head
                    while tail.next != self.head:
                        tail = tail.next
                    if self.head == self.head.next:
                        self.head = None  # only one node
                    else:
                        tail.next = self.head.next
                        self.head = self.head.next
                return
            prev = current
            current = current.next
            if current == self.head:
                break  # key not found

    def search(self, key):
        if not self.head:
            return False
        current = self.head
        while True:
            if current.data == key:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def display(self):
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")

# Example usage
cll = CircularLinkedList()
cll.insert(3)
cll.insert(5)
cll.insert(12)
cll.insert(2)
cll.display()

cll.delete(5)
cll.display()

print("Search 12:", cll.search(12))
print("Search 99:", cll.search(99))