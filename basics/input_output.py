# Python Practice: Input and Output
# Instructions: Use input(), print(), and formatted output to solve each question.

# 1. Ask the user for their name and print a welcome message.
name = input("Enter your name: ")

print("Welcome", name)


# 2. Ask the user for their city and print: "I live in <city>."
city = input("Enter your city: ")

print("I live in", city)


# 3. Ask the user for their favorite food and print it.
food = input("Enter your favorite food: ")

print("Favorite food:", food)


# 4. Ask the user for their favorite programming language and print a sentence using it.
programming = input("Enter your favorite programming language: ")

print("Your favorite programming language:", programming)


# 5. Ask the user for their age and print the entered value.
age = int(input("Enter your age: "))

print("Age:", age)


# 6. Ask the user for their college name and print a formatted message.
college_name = input("Enter your college name: ")

print("You are student of", college_name)


# 7. Ask the user for their first name and last name and print the full name.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = first_name + " " + last_name

print("Full Name:", full_name)


# 8. Ask the user for their name and age and print both values on the same line.
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Name: {name}, Age: {age}")


# 9. Ask the user for three favorite colors and print them.
color1 = input("Enter first color: ")
color2 = input("Enter second color: ")
color3 = input("Enter third color: ")

print(f"First colors: {color1}, Second colors: {color2}, Third colors: {color3}")


# 10. Ask the user for the name of a product and print a simple product label.
product = input("Enter product name: ")

price = 100

print(f"Product: {product}, Price: {price}")


# 11. Ask the user for two numbers and print the values entered.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"First number: {num1}, Second number: {num2}")


# 12. Ask the user for their birth year and print a sentence containing it.
birth_year = int(input("Enter your birth year: "))

print(birth_year, "is your birth year.")


# 13. Ask the user for their country and state, then print both using an f-string.
country = input("Enter your country: ")
state = input("Enter your state: ")

print(f"Country: {country}, State: {state}")


# 14. Ask the user for their name and print it three times on separate lines.
name = input("Enter your name: ")

for i in range(3):
    print(name)

# 15. Ask the user for their favorite movie and favorite actor, then print both.
movie = input("Enter your favorite movie: ")
actor = input("Enter your favorite actor: ")

print(f"Favorite movies: {movie}, Favorite actor: {actor}")


# 16. Ask the user for a word and print its first character and last character.
word = input("Enter a word: ")

print("First Character: ", word[0])
print("Last Character: ", word[-1])


# 17. Ask the user for a sentence and print the sentence in uppercase.
sentence = input("Enter a sentence: ")

print(sentence.upper())

# 18. Ask the user for a sentence and print the sentence in lowercase.
print(sentence.lower())


# 19. Ask the user for their name and course, then display:
#     Name: ...
#     Course: ...
name = input("Enter your name: ")
course = input("Enter your course: ")

print("------- Student Information -------")
print("Student Name:", name)
print("Course:", course)


# 20. Ask the user for the name, age, and city of a person and display all three in a formatted message.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print("------- User Info -------")
print("Name:", name)
print("Age:", age)
print("City:", city)


# 21. Ask the user for two numbers and print their sum.
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

print("Total:", number1 + number2)


# 22. Ask the user for length and width and print a message showing both values.
length = int(input("Enter a length of shape: "))
width = int(input("Enter a width of shape: "))

print(f"{length} is the length of shape and {width} is the width of shape")


# 23. Ask the user for the price of a product and quantity purchased, then print both values.
price = int(input("Enter a product price: "))
quantity = int(input("Enter a product quantity: "))

print(f"Price of product: {price}, and quantity of product: {quantity}")


# 24. Ask the user for three subject names and print them in a single formatted sentence.
subject1 = input("Enter first subject name: ")
subject2 = input("Enter second subject name: ")
subject3 = input("Enter third subject name: ")

print(f"{subject1} is first subject, {subject2} is second subject and {subject3} is third subject name")


# 25. Create a simple "Student Information" program that asks for:
#     Name
#     Age
#     Course
#     College
#     City
#     Then display all information neatly.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")
college = input("Enter your college name: ")
city = input("Enter your city: ")

print("-------- Student Information -------")
print("Student Name:", name)
print("Age:", age)
print("Course:", course)
print("College:", college)
print("City:", city)
