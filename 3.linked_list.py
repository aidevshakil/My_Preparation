# 1. First the Node class
class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Address of the next node, starting with None


# 2. Then the Linked List class
class LinkedList:
    def __init__(self):
        self.head = None  # Initially the list is empty

    # Function to print the list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")


# make empty list
llist = LinkedList()

# make 3 nodes
llist.head = Node(10)
second = Node(20)
third = Node(30)

# addresses link
llist.head.next = second
second.next = third

# print the linked list
llist.print_list()