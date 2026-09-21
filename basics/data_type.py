# Python Practice: Data Types
# Topic: int, float, str, bool, list, tuple, set, dict, None, type()

# 1. Create an integer variable named age and print its value and data type.
age = 24

print(age)
print(type(age))


# 2. Create a float variable named height and print its value and data type.
height = 5.8

print(height)
print(type(height))


# 3. Create a string variable named name and print its value and data type.
name = "Anujith"

print(name)
print(type(name))


# 4. Create a boolean variable named is_student and print its value and data type.
is_student = True

print(is_student)
print(type(is_student))


# 5. Create a list of five fruits and print the list and its data type.
fruits = ['Apple', 'Mango', 'Banana', 'Orange', 'Grapes']

print(fruits)
print(type(fruits))

# 6. Create a tuple containing three numbers and print the tuple and its data type.
numbers = (20, 30, 11)

print(numbers)
print(type(numbers))

# 7. Create a set containing five unique numbers and print the set and its data type.
uniq_num = {10, 20, 30, 40, 50}

print(uniq_num)
print(type(uniq_num))


# 8. Create a dictionary containing your name, age, and city. Print it and its data type.
dic1 = {
    "name": "Anujith",
    "age": 24, 
    "city": "Rajgir"
}

print(dic1)
print(type(dic1))


# 9. Create a variable with the value None and print its value and data type.
v = None

print(v)
print(type(v))


# 10. Create two integer variables and print their sum and the data type of the result.
a = 20
b = 11

int_sum = a + b

print(int_sum)
print(type(int_sum))


# 11. Create two float variables and print their sum and the data type of the result.
value1 = 20.24
value2 = 30.21

float_sum = value1 + value2

print(float_sum)
print(type(float_sum))


# 12. Create an integer and a float. Add them and check the data type of the result.
int_val = 20
float_val = 30.11

total = int_val + float_val

print(total)
print(type(total))


# 13. Create a string containing your favorite programming language and print its length.
programming = "Python"

print(programming)
print(len(programming))


# 14. Create a list of five numbers and print the first and last elements.
list1 = [20, 30, 11, 24, 21]

print(list1[0])     # first element
print(list1[-1])    # last element


# 15. Create a tuple of four colors and print the second element.
colours = ('Red', 'Blue', 'Green', 'Yellow')

print(colours[1])


# 16. Create a set of numbers with one duplicate value. Print the set and observe the result.
set1 = {20, 30, 40, 20,11}

print(set1)


# 17. Create a dictionary for a student with keys: name, age, course, and city. Print each value.
student = {
    "name": "Anujith",
    "age": 24,
    "course": "MCA",
    "city": "Patna"
}

print(student["name"])
print(student["age"])
print(student["course"])
print(student["city"])


# 18. Create three variables containing an integer, float, and string. Print the type of each variable.
age = 21
height = 5.4
name = "Anujith"

print(age, type(age))
print(height, type(height))
print(name, type(name))

# 19. Create a boolean variable and use it in an if statement.
is_student = True

if is_student:
    print("I am student")

# 20. Create a list containing different data types: integer, float, string, and boolean. Print it.
lis = [30, 20.11, 'Komal', True]

print(lis)

# 21. Create a dictionary where one value is a list of three subjects. Print the subjects.
dic = {
    "name": "Anujith",
    "age":24,
    "subject": ["Math", "English", "Science"]

}

print(dic["subject"])

# 22. Create a nested list containing two lists. Print the second element of the first list.
nested_list = [
    [20, 12, 45, 82],
    [30, 11, 78, 24]
]
print(nested_list[0][1])


# 23. Create a variable with a large integer value and check its type.
large_num = 987654321234567890

print(large_num)
print(type(large_num))


# 24. Create a string containing a number, such as "100", and check its data type without converting it.
str1 = "100"

print(type(str1))


# 25. Create variables of at least five different Python data types and print each variable with its type.
age = 24
height = 5.8
name = "Anujith"
is_student = True
fruits = ["Apple", "Mango", "Banana"]
colors = ("Red", "Blue")
numbers = {10, 20, 30}
student = {"name": "Anujith", "age": 24}

print(age, type(age))
print(height, type(height))
print(name, type(name))
print(is_student, type(is_student))
print(fruits, type(fruits))
print(colors, type(colors))
print(numbers, type(numbers))
print(student, type(student))
