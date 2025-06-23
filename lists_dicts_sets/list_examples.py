# -----------------------------------------
# Python Collections: Lists, Dictionaries, Sets, Tuples
# -----------------------------------------

# ============ LISTS ============

# Create a list
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# Access elements
print("First fruit:", fruits[0])

# Modify elements
fruits[1] = "orange"
print("Modified fruits:", fruits)

# Add elements
fruits.append("grape")
fruits.insert(1, "kiwi")
print("After append/insert:", fruits)

# Remove elements
fruits.remove("apple")
last = fruits.pop()
print("After remove & pop:", fruits, "| Popped:", last)

# Check if exists
print("banana" in fruits)

# List slicing
print("First two:", fruits[:2])
print("Reversed list:", fruits[::-1])

# Looping
for fruit in fruits:
    print("Fruit:", fruit)

# List comprehension
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# Nested list
matrix = [[1, 2], [3, 4]]
print("Matrix:", matrix[1][0])  # 3

# ============ DICTIONARIES ============

# Create dictionary
student = {"name": "Oghuz", "age": 22, "is_active": True}
print("Student info:", student)

# Access and modify
print("Name:", student["name"])
student["age"] = 23
print("Updated age:", student["age"])

# Add new key
student["major"] = "Data Science"
print("Added major:", student)

# Remove key
del student["is_active"]
print("After deletion:", student)

# Loop through dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# Safe access
print("Country:", student.get("country", "Not specified"))

# ============ SETS ============

# Create a set
unique_nums = {1, 2, 3, 2, 1}
print("Unique numbers:", unique_nums)

# Add/remove elements
unique_nums.add(4)
unique_nums.discard(2)
print("Modified set:", unique_nums)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

# Check membership
print("3 in set1:", 3 in set1)

# ============ TUPLES ============

# Create a tuple
coordinates = (4, 5)
print("Coordinates:", coordinates)

# Access tuple
print("X:", coordinates[0])

# Nested tuple
point = (4, 5, ("north", "east"))
print("Direction:", point[2][0])

# Tuple unpacking
x, y = coordinates
print("x:", x, "| y:", y)

# Tuple is immutable
# coordinates[0] = 10  # ❌ This would raise an error

# Use as dict key
location = {(4, 5): "Park", (6, 8): "Library"}
print("Location of (4,5):", location[(4, 5)])
