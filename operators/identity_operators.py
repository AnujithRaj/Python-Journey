# Identity Operators — Practice Questions

# 1. Create a = [1, 2, 3] and b = a. Check a is b.
a = [1, 2, 3]
b = a

print(a is b)

# 2. Create a = [1, 2, 3] and b = [1, 2, 3]. Check a is b.
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)

# 3. Create a = [1, 2, 3] and b = a. Check a is not b.
a = [1, 2, 3]
b = a

print(a is not b)

# 4. Create two separate lists with the same values and compare == and is.
lis1 = [2, 5, 8, 9]
lis2 = [2, 5, 8, 9]

print(lis1 == lis2)
print(lis1 is lis2)

# 5. Create x = None and check x is None.
x = None

print(x is None)

# 6. Create x = None and check x is not None.
x = None

print(x is not None)

# 7. Create two dictionary references and test their identity.
dict1 = {
    "name": "Anujith",
    "city": "Rajgir"
}
dict2 = dict1

print(dict1 is dict2)

# 8. Create two tuple variables with the same values and compare identity.
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)

print(tuple1 == tuple2)
print(tuple1 is tuple2)

# 9. Create a list reference and modify it through the second variable. Observe both variables.
list1 = [10, 20, 30]
list2 = list1

list2.append(40)

print(list1)
print(list2)


# 10. Create a shallow copy of a list using copy() and compare is and ==.
list1 = [1, 2, 3]
list2 = list1.copy()

print(list1 == list2)
print(list1 is list2)

# 11. Create a string variable and assign it to another variable. Test identity.
name1 = "Siddharth"
name2 = name1

print(name1 is name2)

# 12. Create two integer variables with the same value and test identity. Observe the result.
x = 100
y = 100

print(x is y)

# 13. Use is to check whether a variable is None before processing it.
value = None

if value is None:
    print("No value available")
else:
    print("Processing value...")

# 14. Use is not to check whether a variable contains an object.
value = [10, 20, 30]

if value is not None:
    print("Object is available")

# 15. Create an object with object() and compare two references using is.
a = object()
b = object()

print(a is b)

# 16. Create a = object() and b = a. Test a is b.
a = object()
b = a

print(a is b)

# 17. Create two object() instances and test whether they are identical.
obj1 = object()
obj2 = object()

print(obj1 is obj2)

# 18. Compare two lists using == and is and explain the difference in comments.
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)
print(list1 is list2)

# 19. Write a small example showing that identity checks object identity, not value equality.
a = [5, 10, 15]
b = [5, 10, 15]

print(a == b)
print(a is b)

# 20. Create three variables and perform both is and is not checks where appropriate.
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
print(a is not c)