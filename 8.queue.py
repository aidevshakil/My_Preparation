from collections import deque
from time import sleep

# রেস্টুরেন্টের কিচেনের কিউ
kitchen_queue = deque()

print("Restaurant opens! Kitchen is operational\n")


# Customers are placing orders
def customer_order():
    orders = [
        "Biryani - Rahim",
        "Fried Rice - Karim",
        "Pizza - Jabbar",
        "Burger - Sohel",
        "Korma - Fahim",
    ]

    for order in orders:
        print(f"New order received: {order}")
        kitchen_queue.append(order)  # enqueue the order
        sleep(2)  # Every 2 seconds a new order comes in


# Chef is cooking (FIFO)
def chef_cooking():
    print("\nChef has started cooking...\n")

    while kitchen_queue:
        current_order = kitchen_queue.popleft()  # Remove the first order
        print(f"Cooking → {current_order}")
        sleep(3)  # Cooking takes 3 seconds
        print(f"Cooking complete! {current_order} is ready\n")

    print("All orders are complete! Kitchen is closed.")


# Main program
customer_order()  # Customers are placing orders
chef_cooking()  # Chef is cooking
