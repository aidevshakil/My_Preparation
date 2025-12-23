class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # add a node
    def append(self, data):
        new_node = Node(data)

        # if list is empty
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # link to itself
            return

        # find the last node
        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head  # link last to first

    # print the entire list (one loop)
    def print_list(self):
        if not self.head:
            print("Empty!")
            return

        current = self.head
        print("Song list (Looping):")
        while True:
            print(current.data, end=" → ")
            current = current.next
            if current == self.head:
                break
        print("Back to start →", self.head.data, "(Loop!)")


cll = CircularLinkedList()
cll.append("wet eyes")
cll.append("you are everywhere")
cll.append("I have water")
cll.append("remembering")

cll.print_list()
