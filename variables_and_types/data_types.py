# -----------------------------------------
# Basic Data Types in Python - Examples
# -----------------------------------------

# Integer
age = 25
year = 2025

# Float 
height = 1.75
pi = 3.14159

# String 
name = "Oghuz"
greeting = "Hello, World!"

# Boolean 
is_student = True
has_passed = False

# NoneType 
value = None

# -----------------------------------------
# Printing and checking types
# -----------------------------------------
print("Age:", age, "| Type:", type(age))          # <class 'int'>
print("Height:", height, "| Type:", type(height))  # <class 'float'>
print("Name:", name, "| Type:", type(name))        # <class 'str'>
print("Is Student:", is_student, "| Type:", type(is_student))  # <class 'bool'>
print("Value:", value, "| Type:", type(value))     # <class 'NoneType'>

# -----------------------------------------
# Type conversion
# -----------------------------------------
# int to float
x = float(age)
print("Converted to float:", x)

# float to int
y = int(height)
print("Converted to int:", y)

# string to int
s = "123"
s_int = int(s)
print("String to int:", s_int)

# int to string
num_str = str(age)
print("Int to string:", num_str)
