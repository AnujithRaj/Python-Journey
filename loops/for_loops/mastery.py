# Print a pyramid star pattern.
rows = 8
for row in range(rows):
    for space in range(rows - row - 1):
        print(" ", end=" ")
    for star in range(2 * row + 1):
        print("*", end=" ")
    print()


# Print an inverted Pyramid.
for row in range(rows):
    for space in range(row):
        print(" ", end=" ")
    for star in range(2 * (rows - row) - 1):
        print("*", end=" ")
    print()


# Print a diamond pattern.
for row in range(rows):
    for i in range(rows - row -1):
        print(" ", end=" ")
    for j in range(2 * row+1):
        print("*", end=" ")
    print()

for row in range(rows -2, -1, -1):
    for k in range(rows - row-1):
        print(" ", end=" ")
    for l in range(2 * row+1):
        print("*", end=" ")
    print()


# Find frequency of each character in a string.
string = input("Enter a String to count Character: ")

freq = {}
for i in string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)


# Find frequency of each element in a list.
lst = input("Enter List elements: ").split()

frq = {}

for i in lst:
    if i in frq:
        frq[i] = frq[i] +1
    else:
        frq[i] = 1

print("Frequency:", frq)


# Remove duplicates from a list using loops.
lis = input("Enter List element with duplicate: ").split()

uniq = []

for i in lis:
    if i not in uniq:
        uniq.append(i)

print("List after removing duplicates: ", uniq)


# Implement list comprehension logic using only for loops.
numbers = [1, 2, 3, 4, 5]

sqr = []

for i in numbers:
    sqr.append(i * i)

print("Squares: ", sqr)


# Flatten a nested list using loops.
nested = [[1,2], [3, 4], [5, 6]]

flat = []

for sublist in nested:
    for item in sublist:
        flat.append(item)

print("Flatten List:", flat)


# Create a simple menu-driven program using loops.
for attempt in range(5):  # Menu show
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Sum:", a + b)

    elif choice == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Difference:", a - b)
    elif choice == 3:
        print("Program Ended")
        break
    else:
        print("Invalid Choice")
        

# Build a mini ATM simulation using loops.
balance = 10000

for i in range(10): # ATM operations allowed 10 times
    print("\n 1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        balance += amount
        print("Deposit Successful")

    elif choice == 3:
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid Choice")

