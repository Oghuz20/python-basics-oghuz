# -----------------------------------------
# Python Object-Oriented Programming (OOP)
# -----------------------------------------

# ============ BASIC CLASS ============

class Person:
    def __init__(self, name, age):
        self.name = name      # Instance variable
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

# Create an object
person1 = Person("Oghuz", 22)
person1.greet()

# ============ CLASS VARIABLES ============

class Student:
    university = "Baku Higher Oil School"  # Class variable (shared)

    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"{self.name} studies at {Student.university}")

s1 = Student("Ali")
s2 = Student("Nigar")
s1.info()
s2.info()

# ============ INHERITANCE ============

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

dog1 = Dog("Rex")
dog1.speak()  # Overrides parent method

# ============ super() EXAMPLE ============

class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")

child1 = Child()

# ============ ENCAPSULATION ============

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

acc = BankAccount("Oghuz", 100)
acc.deposit(50)
acc.withdraw(30)
print("Balance:", acc.get_balance())
# print(acc.__balance)  ❌ Will raise error

# ============ @staticmethod AND @classmethod ============

class MathTools:
    @staticmethod
    def square(x):
        return x * x

    @classmethod
    def info(cls):
        print("This is a math utility class")

print("Square of 5:", MathTools.square(5))
MathTools.info()

# ============ DUNDER METHODS ============

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}"

    def __len__(self):
        return self.pages

book = Book("Python 101", 250)
print(book)          # __str__
print(len(book))     # __len__

# ============ INHERIT MULTI-LEVEL ============

class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Car is driving")

class ElectricCar(Car):
    def charge(self):
        print("Charging battery...")

tesla = ElectricCar()
tesla.move()
tesla.charge()
