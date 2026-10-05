import math
# Topic: Constructors and __init__

# 1. Create a Student class with an __init__ method that accepts name and age.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return self.name, self.age


s1 = Student("Anujith", 22)

print(s1.display())

# 2. Create a Car class whose constructor accepts brand and model.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show(self):
        return self.brand, self.model

c1 = Car("BMW", "X7")
c2 = Car("Mercedes", "Benz")

print(c1.show())
print(c2.show())

# 3. Create a Rectangle class whose constructor accepts length and width.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rec1 = Rectangle(20, 11)

print(rec1.area())

# 4. Create a Person class with a constructor that sets name and city.
class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def display(self):
        return self.name, self.city

p1 = Person("Siddharth", "Rajgir")

print(p1.display())

# 5. Create a Product class with name and price initialized through __init__.
class Product:
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    def details(self):
        return self.product_name, self.product_price

item1 = Product("Water Bottle", 299)

print(item1.details())

# 6. Create an Employee class whose constructor sets name, department, and salary.
class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        return self.name, self.department, self.salary

emp1 = Employee("Siddharth", "HR", 120000)

print(emp1.display())

# 7. Create a BankAccount class with a constructor that sets account holder and balance.
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def show(self):
        return self.account_holder, self.balance

ac1 = BankAccount("Priti", 240000)

print(ac1.show())

# 8. Create a Book class with title, author, and price initialized in the constructor.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        return self.title, self.author, self.price

b1 = Book("Godan", "Munshi Premchand", 299)

print(b1.display())

# 9. Create a Mobile class with brand and storage initialized through __init__.
class Mobile:
    def __init__(self, brand, storage):
        self.brand = brand
        self.storage = storage

    def show(self):
        return self.brand, self.storage

m1 = Mobile("Apple", 256)

print(m1.show())

# 10. Create a Circle class with radius initialized through the constructor and calculate area.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

c1 = Circle(30)

print(c1.area())

# 11. Create a Student class with default age when age is not provided.
class Student:
    def __init__(self, name, city, age=20):
        self.name = name
        self.city = city
        self.age = age

    def display(self):
        return self.name, self.city, self.age

s1 = Student("Priti", "Bhui")

print(s1.display())

# 12. Create a Laptop class with default RAM value of 8 GB.
class Laptop:
    def __init__(self, brand, storage, ram = 8):
        self.brand = brand
        self.storage = storage
        self.ram = ram

    def show(self):
        return self.brand, self.storage, self.ram

l1 = Laptop("Apple", 512)

print(l1.show())

# 13. Create a Person class with a constructor that accepts only name and sets city to a default value.
class Person:
    def __init__(self, name, city = "patna"):
        self.name = name
        self.city = city

    def display(self):
        return self.name, self.city

p1 = Person("Ram")

print(p1.display())

# 14. Create an Employee class with a default salary and print employee details.
class Employee:
    def __init__(self, name, age, city, salary = 60000):
        self.name = name
        self.age = age
        self.city = city
        self.salary = salary

    def details(self):
        return self.name, self.age, self.city, self.salary

emp1 = Employee("Shubham", 24, "Nalanda", 80000)
emp2 = Employee("Komal", 21, "Bhui",)

print(emp1.details())
print(emp2.details())

# 15. Create a Movie class with title, genre, and rating passed to the constructor.
class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def show(self):
        return self.title, self.genre, self.rating

movie1 = Movie("Demon Slayer", "Anime", 8.9)

print(movie1.show())

# 16. Create a Temperature class that initializes Celsius and provides a conversion method.
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

temp1 = Temperature(40)

print(temp1.to_fahrenheit())

# 17. Create a Course class with course name and duration initialized by __init__.
class Course:
    def __init__(self, course_name, course_duration):
        self.course_name = course_name
        self.course_duration = course_duration

    def show(self):
        return self.course_name, self.course_duration

course1 = Course("Data Science", "7 Months")

print(course1.show())

# 18. Create a Team class with team name and number of players initialized in the constructor.
class Team:
    def __init__(self, team_name, no_players):
        self.team_name = team_name
        self.no_players = no_players

    def show(self):
        return self.team_name, self.no_players

tm1 = Team("Patna Pirates", 11)

print(tm1.show())

# 19. Create a BankAccount class that validates that the initial balance is not negative.
class BankAccount:
    def __init__(self, account_holder, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.account_holder = account_holder
        self.balance = balance

    def display(self):
        return self.account_holder, self.balance

ac1 = BankAccount("Komal", 480000)
print(ac1.display())

# 20. Create a Product class and create three objects using different constructor values.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        return self.name, self.price

p1 = Product("Pen", 20)
p2 = Product("Book", 100)
p3 = Product("Watch", 500)

print(p1.show())
print(p2.show())
print(p3.show())
