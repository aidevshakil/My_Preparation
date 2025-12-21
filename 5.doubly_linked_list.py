class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # next node
        self.prev = None  # previous node


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # added at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    # print forward
    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ↔ ")
            current = current.next
        print("None")

    # print backward (only possible in Doubly)
    def print_backward(self):
        if not self.head:
            return

        # go to last node
        current = self.head
        while current.next:
            current = current.next

        # now print backward
        while current:
            print(current.data, end=" ↔ ")
            current = current.prev
        print("None")


dll = DoublyLinkedList()
dll.append("Inside and outside of me")
dll.append("You are everywhere")
dll.append("Oh, my country's soil")
dll.append("A word from mother")

print("Print forward (Next Next):")
dll.print_forward()

print("\nPrint backward (Previous Previous):")
dll.print_backward()