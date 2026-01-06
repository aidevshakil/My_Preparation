# Python's dict is a hash table.
my_dict = {}
my_dict["apple"] = "fruit"  # Store with hash("apple")
print(my_dict["apple"])  # O(1) access


# Custom simple hash function (for strings)
def simple_hash(key, table_size):
    return sum(ord(char) for char in key) % table_size  # Sum of ordinals mod table_size


table = [None] * 10
key = "apple"
index = simple_hash(key, 10)
table[index] = key  # Store
print(table[index])  # apple