# Arithmetic Operators — Practice Questions

# 1. Create two variables a = 15 and b = 4. Print their sum.
a = 15
b = 4

print("Sum:", a + b)


# 2. Create two variables a = 15 and b = 4. Print their difference.
print("Difference:", a - b)


# 3. Create two variables a = 15 and b = 4. Print their product.
print("Product:", a * b)

# 4. Create two variables a = 15 and b = 4. Print the result of true division.
print("Division:", a / b)

# 5. Create two variables a = 15 and b = 4. Print the floor division result.
print("Floor Division:", a // b)


# 6. Create two variables a = 15 and b = 4. Print the remainder.
print("Remainder:", a % b)


# 7. Create two variables a = 2 and b = 5. Print a raised to the power b.
a = 2
b = 5

power = a ** b
print("Power:", power)

# 8. Calculate the area of a rectangle using length = 12 and width = 5.
length = 12
width = 5

print("Area of Rectangle:", length * width)

# 9. Calculate the perimeter of a rectangle using length = 12 and width = 5.
print("Perimeter of rectangle:", 2 * (length + width))


# 10. Calculate the area of a circle using radius = 7. Use 3.14 for pi.
radius = 7

print("Area of circle:", 3.14 * radius * radius)


# 11. Calculate the average of 10, 20, 30, 40, and 50.
num1 = 10
num2 = 20
num3 = 30
num4 = 40
num5 = 50

average = (num1 + num2 + num3 + num4 + num5) / 5

print("Average:", average)

# 12. Calculate the total price of 3 items costing 120, 250, and 80.
item1 = 120
item2 = 250
item3 = 80

print("Price of 3 items:", item1 + item2 + item3)


# 13. Calculate the simple interest for P = 5000, R = 6, T = 2.
p = 5000
r = 6
t = 2

si = (p * r * t) / 100

print("Simple Interest:", si)

# 14. Convert 150 minutes into hours and remaining minutes using // and %.
minutes = 150

hours = minutes // 60
remaining_minutes = minutes % 60

print(f"Hours: {hours} and Minutes: {remaining_minutes}")


# 15. Calculate the final bill when price = 800 and discount = 10 percent.
price = 800
discount = 10

final_bill = price - (price * 10 / 100)

print("Final bill:", final_bill)

# 16. Calculate BMI using weight = 65 kg and height = 1.70 m.
weight = 65
height = 1.70

bmi = weight / (height * height)

print("BMI:", bmi)


# 17. Find the last digit of 9876 using the modulus operator.
digit = 9876

last_digit = digit % 10

print("Last digit:", last_digit)


# 18. Calculate 2 raised to the power 10.
result = 2 ** 10
print("Result:", result)

# 19. Given total_seconds = 7384, find hours, minutes, and seconds using // and %.
total_seconds = 7384

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")

# 20. Write an expression that calculates the result of (25 + 5) * 2 - 10 / 5.
expression = (25 + 5) * 2 - 10 / 5

print("Result:", expression)
