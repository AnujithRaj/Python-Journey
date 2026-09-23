# Python Practice: Type Casting
# Instructions: Practice int(), float(), str(), and bool().

# 1. Convert the string "100" into an integer and print its type.
str_num = "100"
int_num = int(str_num)

print(int_num, type(int_num))


# 2. Convert the string "25.5" into a float and print its type.
str_float = "25.5"
float_num = float(str_float)

print(float_num, type(float_num))


# 3. Convert the integer 50 into a float and print the result.
i_num = 50
f_num = float(i_num)

print(f_num, type(f_num))


# 4. Convert the float 75.8 into an integer and print the result.
f_number = 75.8 
i_number = int(f_number)

print(i_number)


# 5. Convert the integer 100 into a string and print its type.
int1 = 100
str1 = str(int1)

print(str1, type(str1))


# 6. Convert the float 45.6 into a string and print its type.
float_number = 45.6
str_number = str(float_number)

print(str_number, type(str_number))


# 7. Convert the string "123" into an integer and add 10 to it.
str2 = "123"
int2 = int(str2) + 10

print(int2)


# 8. Convert the string "12.5" into a float and multiply it by 2.
str3 = "12.5"
float3 = float(str3) * 2

print(float3)


# 9. Convert the integer 25 into a string and concatenate it with the string " years".
integer_num = 25
string_num = str(integer_num) + " years"

print(string_num)


# 10. Ask the user for their age and convert the input into an integer.
age = input("Enter your age: ")
int_age = int(age)

print("Age:", int_age)
print(type(int_age))

# 11. Ask the user for a decimal number and convert it into a float.
decimal_num = input("Enter a decimal number: ")
float_dec = float(decimal_num)

print(float_dec)


# 12. Ask the user for two numbers as input, convert both to integers, and print their sum.
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

total = int(num1) + int(num2)

print("Total:", total)


# 13. Ask the user for two decimal numbers, convert them to floats, and print their average.
dec_num1 = input("Enter first decimal number: ")
dec_num2 = input("Enter second decimal number: ")

avg = (float(dec_num1) + float(dec_num2)) / 2

print("Average:", avg)


# 14. Convert the integer 0 to bool and print the result.
int_zero = 0
bool_zero = bool(int_zero)

print(bool_zero)


# 15. Convert the integer 1 to bool and print the result.
int_one = 1
bool_one = bool(int_one)

print(bool_one)


# 16. Convert an empty string to bool and print the result.
empty_str = ""
empty_bool = bool(empty_str)

print(empty_bool)


# 17. Convert a non-empty string such as "Python" to bool and print the result.
programming = "Python"
bool_programming = bool(programming)

print(bool_programming)


# 18. Convert the strings "10", "20", and "30" into integers and calculate their total.
first_num = "10"
second_num = "20"
third_num = "30"

num_total = int(first_num) + int(second_num) + int(third_num)

print("Total:", num_total)


# 19. Ask the user for the price of an item and quantity purchased. Convert both inputs into suitable numeric types and calculate the total price.
item_price = input("Enter item price: ")
item_quantity = input("Enter item quantity: ")

total_bill = float(item_price) * int(item_quantity)

print("Total bill:", total_bill)


# 20. Ask the user for marks in three subjects. Convert the inputs into integers and calculate the total marks.
math = input("Enter Math marks: ")
english = input("Enter English marks: ")
science = input("Enter Science marks: ")

total_marks = int(math) + int(english) + int(science)

print("Total marks:", total_marks)


# 21. Ask the user for marks in three subjects and calculate the average using float conversion.
marks_avg = float(total_marks) / 3

print("Average marks:", marks_avg)


# 22. Convert the float 99.99 into an integer and observe what happens to the decimal part.
decimal_number = 99.99
integer_number = int(decimal_number)

print(integer_number)


# 23. Convert the boolean values True and False into integers and print the results.
bool_value1 = True
bool_value2 = False

int_value1 = int(bool_value1)
int_value2 = int(bool_value2)

print(int_value1)
print(int_value2)


# 24. Convert the integers 0, 1, 2, and -1 into boolean values and print each result.
integer1 = 0
integer2 = 1
integer3 = 2
integer4 = -1

boolean1 = bool(integer1)
boolean2 = bool(integer2)
boolean3 = bool(integer3)
boolean4 = bool(integer4)

print(boolean1, boolean2, boolean3, boolean4)


# 25. Create a small calculator that:
#     - takes two numbers as input
#     - converts them into floats
#     - prints their addition, subtraction, multiplication, and division.
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

print("Addition:", first_number + second_number)
print("Subtraction:", first_number - second_number)
print("Multiplication:", first_number * second_number)
print("Division:", first_number / second_number)

