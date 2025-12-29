from collections import deque


class InputRestrictedQueue:
    def __init__(self):
        self.dq = deque()

    # Can only be inserted from the back. (Input Restricted)
    def enqueue(self, item):
        self.dq.append(item)
        print(f"Enqueued (from back) → {item}")

    # Dequeue from the front (like a normal queue)
    def dequeue_front(self):
        if not self.dq:
            print("Queue empty!")
            return None
        item = self.dq.popleft()
        print(f"Dequeued (from front) → {item}")
        return item

    # Dequeue from the rear (this is the special case!)
    def dequeue_rear(self):
        if not self.dq:
            print("Queue empty!")
            return None
        item = self.dq.pop()  # Remove from rear
        print(f"Dequeued (from rear - urgent!) → {item}")
        return item

    def display(self):
        if not self.dq:
            print("Queue empty")
        else:
            print("Queue status (forward ← backward):", list(self.dq))

    def is_empty(self):
        return len(self.dq) == 0


# ───────────── Real-world example: Hospital waiting list ─────────────
print("=== Patients are coming to the hospital ===\n")
hospital = InputRestrictedQueue()

hospital.enqueue("Rahim (cold)")
hospital.enqueue("Karim (light fever)")
hospital.enqueue("Jabbar (stomach ache)")
hospital.enqueue("Sohel (headache)")

hospital.display()
# Output: ['Rahim (cold)', 'Karim (light fever)', 'Jabbar (stomach ache)', 'Sohel (headache)']

print("\nDoctors usually take from the front:")
hospital.dequeue_front()  # Rahim leaves

print("\nSuddenly, someone is very urgent → dequeued from the rear!")
hospital.dequeue_rear()  # Sohel is taken earlier (even though he came last)

hospital.display()