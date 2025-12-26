class CircularQueue:
    def __init__(self, size):
        self.size = size  # Size of the queue
        self.queue = [None] * size  # Fixed size list
        self.front = 0  # Front index
        self.rear = 0  # Rear index
        self.count = 0  # Number of items

    def enqueue(self, item):
        if self.is_full():
            print("Queue full! No more entries allowed.")
            return False

        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.size  # spin round
        self.count += 1
        print(f"Enqueued → {item}")
        return True

    def dequeue(self):
        if self.is_empty():
            print("Queue empty! Nothing to remove")
            return None

        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size  # spin round
        self.count -= 1
        print(f"Removed → {item}")
        return item

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue empty")
            return
        print("Queue status → ", end="")
        i = self.front
        for _ in range(self.count):
            print(self.queue[i], end=" ")
            i = (i + 1) % self.size
        print()


cq = CircularQueue(5)  # 5 places queue

cq.enqueue("Biryani")
cq.enqueue("Pizza")
cq.enqueue("Burger")
cq.enqueue("Korma")
cq.enqueue("Fried Rice")

cq.display()  # Biryani Pizza Burger Korma Fried Rice

cq.enqueue("Tea")  # This won't fit anymore → Queue full!

cq.dequeue()  # Biryani will be removed (the first one that entered)
cq.dequeue()  # Pizza will be removed

cq.display()  # Burger Korma Fried Rice

# Now there is space again → New items can be added
cq.enqueue("Tea")
cq.enqueue("Coffee")

cq.display()  # Burger Korma Fried Rice Tea Coffee
