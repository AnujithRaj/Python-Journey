# Take a number as input: if positive, check whether it is even or odd, otherwise display whether it is negative or zero.
number = int(input("Enter a number: "))

if number > 0:
    print("Positive Number")
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

elif number < 0:
    print("Negative Number")
else:
    print("Zero")


# Take age as input and check voting eligibility. If age >= 18: check if age >= 60 and print "Senior Citizen Voter", Otherwise print "Regular Voter". else print "Not Eligible".
age = int(input("Enter Your Age: "))

if age >= 18:
    if age >= 60:
        print("Senior Citizen Voter")
    else:
        print("Regular Voter")
else:
    print("Not Eligible")


# Take marks as input. If marks >= 40: Check if marks >= 75 -> distinction, else -> Pass. Else -> Fail.
marks = int(input("Enter Your marks: "))

if marks >= 40:
    if marks >= 75:
        print("Distinction")
    else:
        print("Pass")
else:
    print("Fail")


# Input a Number, if number > 0: Check if it is less than 100. Else display appropriate Message.
num = int(input("Enter a Number: "))

if num > 0:
    if num < 100:
        print("Number is between 1 and 99")
    else:
        print("Number is 100 or greater")
else:
    print("Number is not positive")


# Take temperature as input and Check if temperature > 30: check if temperature > 40. Else display whether it is moderate or cold.
temperature = int(input("Enter current Temperature: "))

if temperature > 30:
    if temperature > 40:
        print("Very Hot Weather")
    else:
        print("Hot Weather")
else:
    if temperature > 20:
        print("Moderate Weather")
    else:
        print("Cold weather")