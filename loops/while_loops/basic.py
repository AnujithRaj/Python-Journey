# Print numbers from 1 to 10 using while loop.
number = 1
while number <= 10:
    print(number)
    number = number+1


# Print numbers from 10 to 1.
num = 10
while num >= 1:
    print(num)
    num = num-1


# Print all even number from 1 to 20.
even = 2
while even <= 20:
    print(even)
    even = even+2


# print all odd numbers from 1 to 20.
odd = 1
while odd <= 20:
    print(odd)
    odd = odd+2


# Print multiplication table of 5
t = 1
while t <= 10:
    print(f"5 x {t} = {5* t}")
    t += 1


# Print squares of numbers from 1 to 10.
sq = 1
while sq <= 10:
    print(sq * sq)
    sq = sq+1


# Print cubes of numbers form 1 to 10.
cub = 1 
while cub <= 10:
    print(cub * cub * cub)
    cub = cub+1


# Find the sum of numbers from 1 to 100.
i = 1
total= 0
while i <= 100:
    total = total + i
    i += 1

print("Sum:", total)
    

# Find the sum of even numbers from 1 to 50.
i = 2
total = 0

while i <= 50:
    total += i
    i += 2
print("Sum of Even:", total)


# Find the sum of odd numbers form 1 to 50.
i = 1
total = 0

while i <= 50:
    total += i
    i += 2

print("Sum of Odd:", total)
