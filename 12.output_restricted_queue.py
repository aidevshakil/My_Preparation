from collections import deque


class OutputRestrictedQueue:
    def __init__(self):
        self.dq = deque()

    # Insertion from behind (normal)
    def enqueue_rear(self, item):
        self.dq.append(item)
        print(f"I entered from behind. → {item}")

    # Insertion from front (this is special!)
    def enqueue_front(self, item):
        self.dq.appendleft(item)
        print(f"I entered from the front (VIP/Emergency) → {item}")

    # Output is restricted from the front only!
    def dequeue(self):
        if not self.dq:
            print("Queue is empty! Nothing to dequeue")
            return None
        item = self.dq.popleft()
        print(f"I dequeued (from the front only) → {item}")
        return item

    def display(self):
        if not self.dq:
            print("Queue is empty")
        else:
            print("Queue (Front ← Rear):", list(self.dq))



print("=== People are entering the Pathan cinema hall. ===\n")
cinema = OutputRestrictedQueue()

# Normal customers enter from the rear gate
cinema.enqueue_rear("Rahim")
cinema.enqueue_rear("Karim")
cinema.enqueue_rear("Jabbar")

# Suddenly, Salman Khan arrives → He is allowed in through the front gate (VIP)
cinema.enqueue_front("Salman Khan (VIP)")

# More people entered from the rear
cinema.enqueue_rear("Sohel")
cinema.enqueue_rear("Fahim")

cinema.display()
# Output: ['Salman Khan (VIP)', 'Rahim', 'Karim', 'Jabbar', 'Sohel', 'Fahim']

print("\nThe movie has started... People are exiting only through the main exit:\n")
cinema.dequeue()  # Salman Khan will exit first (FIFO)
cinema.dequeue()  # Rahim
cinema.dequeue()  # Karim

cinema.display()