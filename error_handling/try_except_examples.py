# -----------------------------------------
# Python Error Handling - Try, Except, Else, Finally
# -----------------------------------------

# ============ BASIC EXAMPLE ============
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print("You must enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("End of basic example\n")

# ============ TRY-EXCEPT-ELSE ============
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input.")
else:
    print("You entered:", age)

# ============ MULTIPLE EXCEPTIONS ============
try:
    nums = [1, 2, 3]
    print(nums[5])
except (IndexError, TypeError) as e:
    print("Caught error:", e)

# ============ CUSTOM EXCEPTION MESSAGE ============
try:
    name = input("Enter your name: ")
    if not name:
        raise ValueError("Name cannot be empty!")
    print("Hello,", name)
except ValueError as ve:
    print("Error:", ve)

# ============ CATCHING ALL EXCEPTIONS (not always recommended) ============
try:
    a = int("abc")
except Exception as e:
    print("An unexpected error occurred:", e)

# ============ TRY-EXCEPT INSIDE LOOP ============
numbers = ["10", "5", "zero", "3"]
for val in numbers:
    try:
        print("10 /", val, "=", 10 / int(val))
    except ValueError:
        print("ValueError: Invalid number:", val)
    except ZeroDivisionError:
        print("ZeroDivisionError: Cannot divide by zero")

# ============ FILE HANDLING EXCEPTION ============
try:
    with open("non_existent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")

# ============ ASSERTIONS ============
def divide(a, b):
    assert b != 0, "Divider must not be zero"
    return a / b

try:
    print("Divide 10 by 0:", divide(10, 0))
except AssertionError as ae:
    print("AssertionError:", ae)

# ============ USER-DEFINED EXCEPTION ============
class TooYoungError(Exception):
    pass

age = 15
try:
    if age < 18:
        raise TooYoungError("You must be at least 18 years old.")
    print("Access granted.")
except TooYoungError as e:
    print("Access denied:", e)
