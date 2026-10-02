# Bitwise Operators — Practice Questions

# 1. Use bitwise AND on 12 and 5 and print the result.
print(12 & 5)

# 2. Use bitwise OR on 12 and 5 and print the result.
print(12 | 5)

# 3. Use bitwise XOR on 12 and 5 and print the result.
print(12 ^ 5)

# 4. Use bitwise NOT on 5 and print the result.
print(~5)

# 5. Left-shift 5 by 1 bit.
print(5 << 1)

# 6. Left-shift 5 by 2 bits.
print(5 << 2)

# 7. Right-shift 20 by 1 bit.
print(20 >> 1)

# 8. Right-shift 20 by 2 bits.
print(20 >> 2)

# 9. Use & to check whether the last bit of an integer is set.
num = 7

print(num & 1)

# 10. Use | to set the second bit of a number.
num = 5
mask = 2

print(num | mask)

# 11. Use ^ to toggle the first bit of a number.
num = 5
mask = 1

print(num ^ mask)

# 12. Use & to find common set bits between 10 and 7.
print(10 & 7)

# 13. Use | to combine the set bits of 10 and 7.
print(10 | 7)

# 14. Use ^ to find different bits between 10 and 7.
print(10 ^ 7)

# 15. Predict the result of 8 << 3 and verify it with Python.
print(8 << 3)

# 16. Predict the result of 64 >> 3 and verify it with Python.
print(64 >> 3)

# 17. Convert 13 and 6 to binary using bin() and apply &.
print(bin(13))
print(bin(6))
print(13 & 6)

# 18. Compare the results of 2 * 2 * 2 and 2 << 3.
print(2 * 2 * 2)
print(2 << 3)

# 19. Use a bitwise operation to determine whether 16 is even.
num = 16

print(num & 1)

# 20. Create two integers and print the results of &, |, ^, ~, <<, and >>.
a = 12 
b = 5

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)
