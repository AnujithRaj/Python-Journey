from datetime import datetime
# Project 1: Student Report Card
    # Input:
        # Name
        # Roll Number
        # 5 Subject Marks
name = input("Enter Student Name: ")
roll_no = int(input("Enter Student Roll-Number: "))
english = int(input("Enter English Marks: "))
science = int(input("Enter Science Marks: "))
maths = int(input("Enter Math Marks: "))
hindi = int(input("Enter Hindi Marks: "))
sanskrit = int(input("Enter Sanskrti Marks: "))

total_marks = english + science + maths + hindi + sanskrit
avg = total_marks / 5.0
percentage = (total_marks / 500) * 100

print("----------Student Report Card----------")
print("Student Name:", name)
print("Student roll-number:", roll_no)
print("Total Marks:", total_marks)
print("Average Marks:", avg)
print("Percentage:", round(percentage, 2), "%")


# Project 2: BMI Calculator
    # Input:
        # Weight (kg)
        # Height (m)
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height ** 2)

print("\n-------- BMI --------")
print("Weight:", weight, "kg")
print("Height:", height, "m")
print("BMI:", round(bmi, 2))

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obesity")



# Project 3: Salary Calculator
    # Input:
            # Basic Salary
    # Output:
        # HRA
        # DA
        # Gross Salary
salary = float(input("Ente Basic Salary: "))

hra = salary * 0.20     # 20% HRA
da = salary * 0.10      # 10% DA

gross_salary = salary + hra + da

print("------ Salary Details ------")
print("Basic Salary:", salary)
print("HRA:", hra)
print("DA:", da)
print("Gross Salary:", gross_salary)


# Project 4: Shopping Bill Generator
    # Input:
        # Product Name
        # Price
        # Quantity
    # Output:
        # Total Bill
product = input("Enter Product Name: ")
price = float(input("Enter Product Price: "))
quantity = int(input("Enter Quantity: "))

total_bill = price * quantity

print("------ Shopping Bill ------")
print("Product:", product)
print("Price:", price)
print("Quantity:", quantity)
print("Total Bill:", total_bill)


# Project 5: Age Calculator
    # Input:
        # Birth Year
birth_year = int(input("Enter Your DOB: "))

current_year = datetime.now().year

age = current_year - birth_year

print("Your Age is:", age)



