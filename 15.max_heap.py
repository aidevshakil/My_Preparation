import heapq

max_heap = []

heapq.heappush(max_heap, -50)
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -90)
heapq.heappush(max_heap, -30)

print(max_heap)  # [-90, -50, -10, 30]

# When you take it out, make it negative again.
print(-heapq.heappop(max_heap))  # 90  → The largest
print(-heapq.heappop(max_heap))  # 50
print(-heapq.heappop(max_heap))  # 10