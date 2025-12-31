import heapq

# I created a Priority Queue (Min-Heap → Smaller number = Higher priority)
pq = []

# (priority, item) is entered like this. Smaller number = more important
heapq.heappush(pq, (3, "General Task"))
heapq.heappush(pq, (1, "Critical – Heart Attack"))
heapq.heappush(pq, (4, "Can Wait"))
heapq.heappush(pq, (2, "Moderately Urgent – Broken Bone"))

# Now, when we pop, the most urgent task will come out first
while pq:
    priority, task = heapq.heappop(pq)
    print(f"Priority {priority} → {task}")
