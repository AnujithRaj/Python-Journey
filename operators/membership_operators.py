# Membership Operators — Practice Questions

# 1. Check whether "a" is present in the string "python".
print("a" in "python")

# 2. Check whether "z" is not present in the string "python".
print("z" not in "python")

# 3. Check whether 3 is present in the list [1, 2, 3, 4].
print(3 in [1, 2, 3, 4])

# 4. Check whether 10 is not present in the list [1, 2, 3, 4].
print(10 not in [1, 2, 3, 4])


# 5. Check whether "apple" is present in a list of fruits.
fruits = ["Mango", "Banana", "Orange", "Grapes", "Pears"]

print("Apple" in fruits)
# 6. Check whether "mango" is not present in a list of fruits.
print("Mango" not in fruits)

# 7. Check whether a username is present in a list of allowed users.
allowed_users = ["Anujith", "Siddharth", "Tripti", "Priti", "Komal"]

username = "Anujith"

print(username in allowed_users)

# 8. Check whether a character is present in a user-entered word.
word = input("Enter a word: ")
character = input("Enter a character: ")

print(character in word)

# 9. Check whether a subject is present in a tuple of subjects.
subjects = ("Python", "SQL", "Math", "Statistics")

print("Python" in subjects)

# 10. Check whether a number is present in a tuple of even numbers.
even_num = (2, 4, 6, 8, 10)

print(6 in even_num)

# 11. Check whether a key is present in a dictionary using in.
student ={
    "name": "Anujith",
    "age": 22,
    "course": "MCA"
}

print("name" in student)

# 12. Check whether a key is not present in a dictionary using not in.
print("marks" not in student)

# 13. Check whether a word is present in a sentence.
sentence = "I am learning Python"

print("Python" in sentence)

# 14. Check whether a file extension ".py" is present in a filename.
filename = "python.py"

print(".py" in filename)

# 15. Check whether the number 0 is present in a list of marks.
marks = [87, 92, 63, 71, 59]

print(0 in marks)

# 16. Check whether "SQL" is present in a list of Data Science skills.
skills = ["Python", "SQL", "Pandas", "Numpy", "Machine Learning"]

print("SQL" in skills)

# 17. Check whether a product category exists in a tuple of categories.
categories = ("Electronics", "Clothing", "Food", "Books")

print("Food" in categories)

# 18. Ask the user for a city and check whether it belongs to a predefined list of cities.
cities = ["Patna", "Delhi", "Mumbai", "Kolkata", "Bangalore"]

city = input("Enter your city: ")

print(city in cities)

# 19. Ask the user for a course name and check whether it is available in a list.
courses = ["Python", "Data Science", "Machine Learning", "Web Development"]

course = input("Enter course name: ")

print(course in courses)

# 20. Create a list and demonstrate both in and not in.
numbers = [10, 20, 30, 40, 50]

print(30 in numbers)
print(100 not in numbers)
