# -----------------------------------------
# Python Conditionals and Loops - Full Guide
# -----------------------------------------

# ============ IF-ELSE STATEMENTS ============

# Simple if
x = 10
if x > 5:
    print("x is greater than 5")

# If-else
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")

# If-elif-else
grade = 82
if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Nested if
age = 20
if age > 18:
    if age < 25:
        print("Young adult")
    else:
        print("Adult")
else:
    print("Minor")

# ============ FOR LOOPS ============

# Basic for loop with range
for i in range(1, 6):
    print("i =", i)

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# Loop through a string
word = "data"
for letter in word:
    print(letter)

# Using enumerate
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Loop with break
for i in range(10):
    if i == 4:
        print("Breaking at 4")
        break
    print("i =", i)

# Loop with continue
for i in range(5):
    if i == 2:
        continue  # Skip when i == 2
    print("i =", i)

# ============ WHILE LOOPS ============

# Basic while loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1

# While True (with break)
while True:
    name = input("Enter your name (or 'q' to quit): ")
    if name == "q":
        print("Goodbye!")
        break
    print("Hello,", name)

# ============ LIST COMPREHENSIONS ============

# Create list of squares
squares = [i**2 for i in range(1, 6)]
print("Squares:", squares)

# Create list of even numbers
evens = [i for i in range(10) if i % 2 == 0]
print("Even numbers:", evens)

# Create list of capitalized fruits
capitalized = [fruit.capitalize() for fruit in fruits]
print("Capitalized fruits:", capitalized)

# Nested list comprehension: multiplication table
table = [f"{i} x {j} = {i*j}" for i in range(1, 4) for j in range(1, 4)]
print("Mini multiplication table:", table)
