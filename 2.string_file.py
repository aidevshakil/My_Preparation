name = "Alice"
age = 25

# regular
regular = "Name: " + name + ", Age: " + str(age)
print(regular)  # Name: Alice, Age: 25

# f-String (advanced formatting and preferred)
f_string = f"Name: {name}, Age: {age}"
print(f_string)  # Name: Alice, Age: 25

# Raw String
raw = r"C:\Users\Alice\Documents"  # skips escape sequences
print(raw)  # C:\Users\Alice\Documents

# Bytes String
bytes_str = b"Hello \xe2\x98\x83"  # Limited Unicode support
print(bytes_str)  # b'Hello \xe2\x98\x83'
