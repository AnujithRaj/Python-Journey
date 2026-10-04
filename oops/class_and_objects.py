import math

# Topic: Classes and Objects

# 1. Create a Student class with name and age attributes and create one object.
class Students:
    def info(self, name, age):
        self.name = name
        self.age = age

s1 = Students()
s1.info("Anujith", 22)

print(s1.name)
print(s1.age)


# 2. Create a Car class with brand and model attributes and print them.
class Car:
    def vehicle(self, brand, model):
        self.brand = brand
        self.model = model

c1 = Car()
c1.vehicle("BMW", "X7")

print(c1.brand)
print(c1.model)

# 3. Create a Person class with name and city attributes and display the values.
class Person:
    def display(self, name, city):
        self.name = name
        self.city = city

p1 = Person()
p1.display("Siddharth", "Rajgir")

print(p1.name)
print(p1.city)

# 4. Create a Book class with title and author attributes and create two objects.
class Books:
    def show(self, title, author):
        self.title = title
        self.author = author

b1 = Books()
b2 = Books()

b1.show("Godan", "Premchand")
b2.show("Maila Anchal", "Faneshwaarnath Renu")

print(b1.title)
print(b1.author)

print(b2.title)
print(b2.author)

# 5. Create a Mobile class with brand and price attributes and display them.
class Mobile:
    def display(self, brand, price):
        self.brand = brand
        self.price = price

m1 = Mobile()
m1.display("Apple", 120000)

print(m1.brand)
print(m1.price)

# 6. Create an Employee class with name and salary attributes and print employee details.
class Employee:
    def details(self, name, salary):
        self.name = name
        self.salary = salary

emp1 = Employee()
emp1.details("Tripti", 60000)

print(emp1.name)
print(emp1.salary)

# 7. Create a Rectangle class with length and width attributes and calculate its area.
class Rectangle:
    def sides(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rec1 = Rectangle()
rec1.sides(20, 11)

print(rec1.area())

# 8. Create a Circle class with a radius attribute and calculate its area.
class Circle:
    def details(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

c1 = Circle()
c1.details(14)

print(c1.area())

# 9. Create a Laptop class with brand, RAM, and storage attributes and display them.
class Laptop:
    def display(self, brand, RAM, storage):
        self.brand = brand
        self.RAM = RAM
        self.storage = storage

l1 = Laptop()
l1.display("Apple", 16, "512")

print(l1.brand)
print(l1.RAM)
print(l1.storage)

# 10. Create a BankAccount class with account_holder and balance attributes.
class BankAccount:
    def details(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

ac1 = BankAccount()
ac1.details("Siddharth", 80000)

print(ac1.account_holder)
print(ac1.balance)

# 11. Create a Movie class with title, genre, and rating attributes.
class Movie:
    def info(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

m1 = Movie()
m1.info("Demon Slayer", "Anime", 8.6)

print(m1.title)
print(m1.genre)
print(m1.rating)

# 12. Create a Product class with name and price attributes and calculate the price after a discount.
class Product:
    def display(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    def discount(self, percentage):
        return self.product_price - (self.product_price * percentage / 100)

p1 = Product()
p1.display("Pen", 20)

print(p1.discount(10))
print(p1.product_name)
print(p1.product_price)

# 13. Create a Dog class with name and breed attributes and create three dog objects.
class Dog:
    def display(self, name, breed):
        self.name = name
        self.breed = breed

d1 = Dog()
d2 = Dog()
d3 = Dog()

d1.display("Pommy", "Indian Spitz")
d2.display("Tommy", "German Shepherd")
d3.display("Leap", "Golden Retriever")

print(d1.name)
print(d2.name)
print(d3.name)

print(d1.breed)
print(d2.breed)
print(d3.breed)

# 14. Create a College class with name and location attributes and display its details.
class College:
    def display(self, name, location):
        self.name = name
        self.location = location

c1 = College()
c1.display("Manipal University", "Jaipur")

print(c1.name)
print(c1.location)

# 15. Create a Temperature class with a Celsius attribute and convert it to Fahrenheit.
class Temperature:
    def display(self, celsius):
        self.celsius = celsius
        self.fahrenheit = (celsius * 9/5) + 32

t1 = Temperature()
t1.display(40)

print(t1.fahrenheit)

# 16. Create a Student class with marks in three subjects and calculate the total.
class Student:
    def display(self, math, science , english):
        self.math = math
        self.science = science
        self.english = english

s1 = Student()
s1.display(82, 86, 78)

total = s1.math + s1.science + s1.english
print(total)

# 17. Create a Laptop class and compare the prices of two laptop objects.
class Laptops:
    def display(self, price):
        self.price = price

l1 = Laptops()
l2 = Laptops()
l1.display(80000)
l2.display(90000)

if l1.price > l2.price:
    print("Laptop 1 is expensive")
elif l2.price > l1.price:
    print("Laptop 2 is expensive")
else:
    print("Both have the same price")


# 18. Create a Bus class with route number and capacity attributes and display them.
class Bus:
    def display(self, route_number, capacity):
        self.route_number = route_number
        self.capacity = capacity

b1 = Bus()
b1.display("Rajgir to Patna", 40)

print(b1.route_number)
print(b1.capacity)

# 19. Create a Book class and count how many book objects you create.
class Book:

    count = 0

    def details(self, name, price):
        self.name = name
        self.price = price
        Book.count += 1

b1 = Book()
b2 = Book()
b3 = Book()

b1.details("abc", 999)
b2.details("xyz", 500)
b3.details("pqr", 750)

print(Book.count)

# 20. Create a simple ShoppingCart class with item name and price attributes.
class ShoppingCart:
    def display(self, item_name, price):
        self.item_name = item_name
        self.price = price

sc1 = ShoppingCart()
sc1.display("Peanut Butter", 499)

print(sc1.item_name)
print(sc1.price)