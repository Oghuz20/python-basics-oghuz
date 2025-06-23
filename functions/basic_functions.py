# -----------------------------------------
# Python Functions – Basics to Advanced
# -----------------------------------------

# ============ BASIC FUNCTION ============
def greet():
    print("Hello from a function!")

greet()

# ============ FUNCTION WITH ARGUMENTS ============
def greet_name(name):
    print(f"Hello, {name}!")

greet_name("Oghuz")

# ============ RETURNING A VALUE ============
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)

# ============ DEFAULT ARGUMENTS ============
def introduce(name, country="Azerbaijan"):
    print(f"My name is {name} and I'm from {country}.")

introduce("Oghuz")
introduce("Elvin", "Turkey")

# ============ KEYWORD ARGUMENTS ============
introduce(country="Germany", name="Ali")

# ============ *ARGS (Variable-Length Arguments) ============
def print_scores(*scores):
    for i, score in enumerate(scores):
        print(f"Score {i+1}: {score}")

print_scores(80, 90, 95)

# ============ **KWARGS (Keyword Variable-Length Arguments) ============
def show_student_info(**info):
    for key, value in info.items():
        print(f"{key.capitalize()}: {value}")

show_student_info(name="Oghuz", age=22, major="Data Science")

# ============ LAMBDA FUNCTIONS ============
# lambda arguments: expression

multiply = lambda x, y: x * y
print("Lambda multiply:", multiply(4, 5))

# ============ MAP FUNCTION ============
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print("Squared with map:", squared)

# ============ FILTER FUNCTION ============
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers with filter:", evens)

# ============ ZIP FUNCTION ============
names = ["Ali", "Nigar", "Oghuz"]
scores = [85, 90, 95]
paired = list(zip(names, scores))
print("Zipped list:", paired)

# ============ ENUMERATE FUNCTION ============
for index, fruit in enumerate(["apple", "banana", "cherry"], start=1):
    print(f"{index}. {fruit}")

# ============ NESTED FUNCTIONS ============
def outer_function(a):
    def inner_function(b):
        return a + b
    return inner_function

add_10 = outer_function(10)
print("Nested function result:", add_10(5))  # Output: 15

# ============ FUNCTION AS ARGUMENT ============
def apply_twice(func, x):
    return func(func(x))

print("Apply twice:", apply_twice(lambda x: x + 1, 3))  # (3+1)+1 = 5

# ============ FUNCTION ANNOTATIONS ============
def divide(a: float, b: float) -> float:
    return a / b if b != 0 else 0.0

print("Division:", divide(10, 2))
