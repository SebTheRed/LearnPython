# CHALLENGE:
# For practice, create a tuple representing a point in 3D space, for example, (x, y, z). Then:
# Print each coordinate using indexing.
# Create a new tuple by slicing the first two elements of the original tuple and print it.
# Try to change one of the coordinates to see what happens (you should encounter a TypeError).

coordinates = (12, 97, -2)
print("X: ", coordinates[0])
print("Y: ", coordinates[1])
print("Z: ", coordinates[2])
xY = coordinates[0:2]
print(xY)
# tupleVariable[1] = 20