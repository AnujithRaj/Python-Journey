# Logical Operators — Practice Questions

# 1. Use and to check whether age = 25 is at least 18 and at most 60.
age = 25

print(age >= 18 and age <= 60)

# 2. Use or to check whether day = "Saturday" or "Sunday".
day = "Saturday"

print(day == "Saturday" or day == "Sunday")

# 3. Use not to reverse the Boolean value True.
print(not True)

# 4. Check whether a number is positive and even using and.
num = 20

print(num > 0 and num % 2 == 0)

# 5. Check whether a number is divisible by 3 or 5 using or.
number = 30

print(number % 3 == 0 or number % 5 == 0)

# 6. Check whether a username is "admin" and password is "1234".
username = "admin"
password = "1234"

print(username == "admin" and password == "1234")

# 7. Check whether marks are at least 40 and attendance is at least 75.
marks = 40
attendance = 75

print(marks >= 40 and attendance >= 75)

# 8. Check whether temperature is below 0 or above 40.
temperature = 32

print(temperature < 0 or temperature > 40)

# 9. Check whether a person is not a minor using not and age < 18.
age = 20

print(not(age < 18))

# 10. Check whether a number is between 10 and 100 using and.
n = 30

print(n >= 10 and n <= 100)

# 11. Check whether a number is outside the range 10 to 100 using not.
n = 30

print(not(n >= 10 and n <= 100))

# 12. Check whether either math_marks or science_marks is at least 90.
math_marks = 85
science_marks = 95

print(math_marks >= 90 or science_marks >= 90)

# 13. Check whether both email and phone are available.
email = True
phone = True

print(email and phone)

# 14. Check whether a user can log in when is_active is True and is_blocked is False.
is_active = True
is_blocked = False

print(is_active and not is_blocked)

# 15. Check whether a product is eligible for free delivery when price >= 500 or membership is True.
price = 450
membership = True
print(price >= 500 or membership == True)

# 16. Combine and, or, and not to check a simple admission condition.
marks = 75
entrance_passed = True
documents_complete = True

print((marks >= 60 and entrance_passed and documents_complete))

# 17. Given raining = True and umbrella = False, check whether going outside is possible.
raining = True
umbrella = False

print(not raining or umbrella)

# 18. Given battery = 80 and charging = False, check whether the device needs charging.
battery = 80
charging = False

print(battery < 20 and not charging)

# 19. Create three Boolean variables and test different logical combinations.
a = True
b = False
c = True

print(a and b)
print(a or b)
print(not c)
print((a and b) or c)

# 20. Write one expression that uses all three logical operators: and, or, and not.
age = 25
student = True
blocked = False

print((age >= 18 and student) or not blocked)
