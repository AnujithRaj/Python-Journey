# Count digits in a number.
n = int(input("Enter a Number: "))

count = 0

while n > 0:
    count += 1
    n //= 10

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

# Reverse a number.

# Check whether a number is a palindrome.

# Find the largest digit in a number.

# Find the smallest digit in a number.

# Count even digits in a number.

# Count odd digits in a number.

# Calculate the average of digits.
