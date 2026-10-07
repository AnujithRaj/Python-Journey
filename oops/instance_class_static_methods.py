# Topic: Instance, Class, and Static Methods

# 1. Create a Student class with an instance method that displays student details.
class Student:
    def __init__(self, name, roll_no, age):
        self.name = name
        self.roll_no = roll_no
        self.age = age

    def display(self):
        return self.name, self.roll_no, self.age

s1 = Student("Hritik", 21, 24)

print(s1.display())

# 2. Create a Calculator class with an instance method to add two numbers.
class Calculator:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def show(self):
        return self.first_number + self.second_number

cal1= Calculator(20, 30)

print(cal1.show())

# 3. Create a School class with a class variable school_name and display it using a class method.
class School:
    school_name = "Prakash Vidya Niketan"

    def __init__(self, location):
        self.location = location

    @classmethod
    def display_school(cls):
        return cls.school_name

sc1 = School("Bhui")

print(sc1.display_school())

# 4. Create an Employee class with a class variable company_name and a class method to change it.
class Employee:
    company_name = "Mart"
    def __init__(self, company_owner, location):
        self.company_owner = company_owner
        self.location = location

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name

    def display(self):
        return self.company_name, self.company_owner, self.location

emp1= Employee("Anujith", "Bhui")

print(emp1.display())

Employee.change_company_name("New Mart")

print(emp1.display())

# 5. Create a MathUtils class with a static method to check whether a number is even.
class MathUtils:

    @staticmethod
    def is_even(number):
        return number % 2 == 0

print(MathUtils.is_even(20))
print(MathUtils.is_even(15))


# 6. Create a Calculator class with static methods for addition and subtraction.
class Calculator:

    @staticmethod
    def addition(num1, num2):
        return num1 + num2

    @staticmethod
    def subtraction(num1, num2):
        return num1 - num2

print(Calculator.addition(20, 30))
print(Calculator.subtraction(20, 11))

# 7. Create a Person class with an instance method that introduces the person.
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduces(self):
        return f" My name is {self.name}, I am {self.age} years old, and I live in {self.city}"

p1 = Person("Siddharth", 24, "Rajgir")

print(p1.introduces())


# 8. Create a Product class with a class variable tax_rate and a method to calculate tax.
class Product:
    tax_rate = 12

    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def tax(self):
        return self.price * Product.tax_rate / 100


p1 = Product("Watch", 1000)

print(p1.tax())

# 9. Create a Student class with a class method that creates a student from a string.
class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    @classmethod
    def from_string(cls, data):
        name, age, city = data.split(",")
        return cls(name, int(age), city)


s1 = Student.from_string("Siddharth,22,Rajgir")

print(s1.name)
print(s1.age)
print(s1.city)

# 10. Create a Temperature class with a static method to convert Celsius to Fahrenheit.
class Temperature:

    @staticmethod
    def show(celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

print(Temperature.show(40))

# 11. Create a Rectangle class with an instance method to calculate area.


# 12. Create a Bank class with a class method to display the total number of accounts.


# 13. Create a Utility class with a static method to validate an email string contains @.


# 14. Create a Book class with a class variable total_books and increment it for each object.


# 15. Create a Circle class with a static method to calculate area from a radius.


# 16. Create an Employee class with an instance method to calculate annual salary.


# 17. Create a Course class with a class method to create an object from a course string.


# 18. Create a Number class with a static method to check whether a number is prime.


# 19. Create a ShoppingCart class with an instance method to calculate total price.


# 20. Create one class demonstrating one instance method, one class method, and one static method.


