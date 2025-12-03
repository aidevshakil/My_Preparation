import array

# make int array
ints = array.array("i", [1, 2, 3, 4])
print(ints[1])  # 2
ints.append(5)
print(ints)  # array('i', [1, 2, 3, 4, 5])
ints.insert(0, 0)  # এখন [0,1,2,3,4,5]
bytes_data = (
    ints.tobytes()
)  # b'\x00\x00\x00\x00\x01\x00\x00\x00...' (binary representation)
print(len(bytes_data))  # 24 bytes (6*4)

# make float array
floats = array.array("f", [1.5, 2.5])
floats.extend([3.5, 4.5])
print(floats)  # array('f', [1.5, 2.5, 3.5, 4.5])
