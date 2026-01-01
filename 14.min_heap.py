import heapq

# Create an empty Min Heap
min_heap = []

# Insertion (heappush)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 8)
heapq.heappush(min_heap, 3)

print(min_heap)  # [1, 3, 8, 5]  → The smallest element is at the front

# Removal (heappop) → The smallest element is removed first
print(heapq.heappop(min_heap))  # 1
print(heapq.heappop(min_heap))  # 3
print(min_heap)  # [5, 8]