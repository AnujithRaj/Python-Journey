# Take a number N and print numbers from 1 to N.
number = int(input("Enter a Number: "))
i = 1

while i <= number:
    print(i)
    i = i+1


# Take N and print numbers from N to 1.
number = int(input("Enter a Number: "))
i = number

while i >= 1:
    print(i)
    i -= 1


# Take N and print all even numbers up to N.
n = int(input("Enter a Number: "))
i = 2

while i <= n:
    print(i)
    i += 2


# Take N and print all odd numbers up to N.
n = int(input("Enter a Number: "))
i = 1

while i <= n:
    print(i)
    i += 2

    
# Take N and find the sum of numbers from 1 to N.
n = int(input("Enter a Number: "))
i = 1

total = 0
while i <= n:
    total = total + i
    i += 1

print("Sum of total number:", total)


# Take N and find the factorial of N.
n = int(input("Enter a Number: "))
i = 1
factorial = 1

while i <= n:
    factorial *= 1
    i += 1

print("Factrorial:", factorial)


# Take N and print its multiplication table.
n = int(input("Enter a Number: "))
i = 1

while i <= 10:
    print(f"{n} x {i} = {n*i}")
    i += 1


# Count how many numbers are printed from 1 to N.
n = int(input("Enter a Number: "))
i = 1
count = 0

while i <= n:
    print(i)
    count += 1
    i += 1

print("Total Numbers Printed:", count)


# Find the product of numbers from 1 to N.
n = int(input("Enter a Number: "))
i = 1
product = 1

while i <= n:
    product *= i
    i += 1

print("Product:", product)


# Print numbers divisible by 3 up to N.
n = int(input("Enter a Number: "))
i = 1

while i <= n:
    if i %3 == 0:
        print(i)
    i += 1
