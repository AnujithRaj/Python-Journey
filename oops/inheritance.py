# Topic: Inheritance

# 1. Create a Person class and inherit a Student class from it.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def show(self):
        return self.name, self.age, self.roll_no

s1 = Student("Siddharth", 22, 4)

print(s1.show())

# 2. Create a Vehicle class and inherit Car from it.
class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

class Car(Vehicle):
    def __init__(self, brand, color, model):
        super().__init__(brand, color)
        self.model = model

    def display(self):
        return self.brand, self.color, self.model

car1 = Car("BMW", "White", "X7")

print(car1.display())

# 3. Create an Animal class and inherit Dog from it.
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Dog(Animal):
    def __init__(self, name, color, sound):
        super().__init__(name, color)
        self.sound = sound

    def display(self):
        return self.name, self.color, self.sound

dog1 = Dog("Pommy", "White", "Boo-Boo")

print(dog1.display())

# 4. Create a parent class Employee and child class Manager.
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Manager(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def details(self):
        return self.name, self.age, self.salary

m1 = Manager("Tripti", 21, 80000)

print(m1.details())

# 5. Create a Shape class and inherit Rectangle from it.
class Shape:
    def __init__(self):
        print("This is a shape")

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        self.area = self.length * self.width

    def show_area(self):
        return self.area

rec1 = Rectangle(20, 11)

print(rec1.show_area())

# 6. Create a BankAccount class and inherit SavingsAccount from it.


# 7. Create a Device class and inherit Mobile from it.


# 8. Create a Person class with a name attribute and access it from a Student object.


# 9. Create a Vehicle class with a start method and use it in a Car child class.


# 10. Create a parent class with a constructor and call it from the child constructor using super().


# 11. Create an Animal class with a sound method and extend it in Dog.


# 12. Create a three-level inheritance example: Animal -> Mammal -> Dog.


# 13. Create a multilevel inheritance example using Grandparent -> Parent -> Child.


# 14. Create a hierarchical inheritance example with Animal as parent and Dog and Cat as children.


# 15. Create a parent class Person and two child classes Student and Teacher.


# 16. Create an Employee class with salary and a Manager class that adds a bonus.


# 17. Create a Vehicle class with speed and a Bike class that adds gear.


# 18. Create a Shape class and child classes Rectangle and Circle with their own area methods.


# 19. Create a parent class Account and child classes SavingsAccount and CurrentAccount.


# 20. Create an inheritance example where the child adds a new method to the parent functionality.

