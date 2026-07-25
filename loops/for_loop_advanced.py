# Find all prime numbers between 1 and 100.
for i in range(2, 101):
    prime = True

    for j in range(2, i):
        if i % j == 0:
            prime = False
            break

    if prime:
        print(i, end=", ")
print()
        
# Check whether a number is prime.
number = int(input("Enter a Number to check Prime: "))

prime = True

if number <= 1:
    prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
if prime:
    print(number, "is a Prime Number")
else:
    print(number, "is not a Prime Number")


# Print Fibonacci series up to N terms.
num = int(input("Enter a number for Fibonacci series: "))
a, b = 0, 1
for i in range(num):
    print(a, end=", ")
    a, b = b, a+b
print()


# Find Armstrong numbers between 1 and 1000.
number1 = int(input("Enter a Number to check Armstrong: "))

num_str = str(number1)
power = len(num_str)

total = 0

for digit in num_str:
    total += int(digit) ** power

if total == number1:
    print(number1, "is an Armstrong Number")
else:
    print(number1, "is not an Armstrong Number")


# Find perfect numbers between 1 and 1000.
num1 = int(input("Enter a Number to check perfect number: "))

sum_divisors = 0

for i in range(1, num1):
    if num1 % i == 0:
        sum_divisors += i

if sum_divisors == num1:
    print(num1, "is a Perfect Number")
else:
    print(num1, "is not a Perfect Number")

    
# Print all divisors of a number.
num2 = int(input("Enter a number to find divisors: "))

for i in range(1, num2+1):
    if num2 % i == 0:
        print(i)


# Find GCD of two numbers using loops.
first_num = int(input("Enter First number of GCD: "))
second_num = int(input("Enter Second number of GCD: "))

gcd = 1

for i in range(1, min(first_num, second_num) +1):
    if first_num % i == 0 and second_num % i == 0:
        gcd = i

print("GCD:", gcd)


# Find LCM of two numbers using loops.
f_num = int(input("Enter first number for lcm: "))
s_num = int(input("Enter second number for lcm: "))

greater = max(f_num, s_num)

for i in range(greater, f_num * s_num + 1):
    if i % f_num == 0 and i % s_num == 0:
        print("LCM:", i)
        break


# Generate a right Pascal triangle pattern.
triangle_rows = int(input("Enter a Triangle Rows: "))

for i in range(1, triangle_rows+1):
    for j in range(i):
        print(j+1, end=" ")
    print()

for i in range(triangle_rows-1, 0, -1):
    for j in range(i):
        print(j+1, end=" ")
    print()


# Generate Floyd's Triangle.
rows = int(input("Enter a triangle rows: "))

element = 1

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(element, end=" ")
        element += 1
    print()
