class Node:
    def __init__(self, data):
        self.data = data  # Store the name/number here
        self.next = None  # Next person's address


# Example: Treasure Hunt
head = Node("Start: Go behind the house.")
head.next = Node("Look under the tree.")
head.next.next = Node("Go to the riverbank.")
head.next.next.next = Node("You've found the treasure chest! 🎉")

# Now let's print it all out.
current = head
while current:
    print(current.data)
    current = current.next
