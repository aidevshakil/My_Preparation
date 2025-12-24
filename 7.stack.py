# empty stack
stack = []

# 1. push → To put something in (put it on top)
stack.append(10)  # stack = [10]
stack.append(20)  # stack = [10, 20]
stack.append(30)  # stack = [10, 20, 30]

print("Stack now:", stack)  # [10, 20, 30]

# 2. pop → Remove the top item
print("Popped:", stack.pop())  # 30 will be popped
print("Stack now:", stack)  # [10, 20]

# 3. peek → Just look at the top item (don't remove it)
print("is above:", stack[-1])  # 20

# 4. Check if empty
if len(stack) == 0:
    print("Stack is empty!")
else:
    print("Stack has", len(stack), "items")
