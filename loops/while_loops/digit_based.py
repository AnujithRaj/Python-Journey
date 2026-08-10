# Count digits in a number.
num = int(input("Enter a Number: "))
num = abs(num)

count = 0

while num > 0:
    count += 1
    num //= 10

print("Number of digits:", count)


# Find the sum of digits of a number.
num = int(input("Enter a Number: "))
num = abs(num)

total = 0

while num > 0:
    digit = num % 10
    total += digit
    num //= 10

print("Sum of digits:", total)


# Find the product of digits of a number.
num = int(input("Enter a Number: "))
num = abs(num)

product = 1

while num > 0:
    digit = num % 10
    product *= digit
    num //= 10

print("Product of digits:", product)


# Reverse a number.
num = int(input("Enter a Number: "))
num = abs(num)

reverse = 0

while num > 0:
    digit = num % 10 
    reverse = reverse * 10 + digit
    num //= 10

    print("Reverse:", reverse)


# Check whether a number is a palindrome.
num = int(input("Enter a Number: "))
num = abs(num)

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")


# Find the largest digit in a number.
num = int(input("Enter a Number: "))
num = abs(num)

largest = 0

while num > 0:
    digit = num % 10

    if digit > largest:
        largest = digit

    num //= 10

print("Largest digit:", largest)


# Find the smallest digit in a number.
num = int(input("Enter a Number: "))
num = abs(num)

smallest = 9

while num > 0:
    digit = num % 10

    if digit < smallest:
        smallest = digit

    num //= 10

print("Smallest digit:", smallest)


# Count even digits in a number.
num = int(input("Enter a Number: "))
num = abs(num)

count = 0

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        count += 1

    num //= 10

print("Even digits:", count)


# Count odd digits in a number.
num = int(input("Enter a Number: "))
num = abs(num)

count = 0

while num > 0:
    digit = num % 10

    if digit % 2 != 0:
        count += 1

    num //= 10

print("Odd digits:", count)


# Calculate the average of digits.
num = int(input("Enter a Number: "))
num = abs(num)

total = 0
count = 0

while num > 0:
    digit = num % 10
    total += digit
    count += 1
    num //= 10

average = total / count

print("Average of digits:", average)
