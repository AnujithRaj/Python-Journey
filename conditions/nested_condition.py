# ATM withdrawal system: Check PIN, Then check balance
balance = 10000
correct_pin = 1234

pin = int(input("Enter ATM PIN: "))

if pin == correct_pin:
    amount = float(input("Enter withdrawal amount: "))

    if amount <= balance:
        balance = balance - amount
        print("Withdrawal Successful!")
        print("Remaining Balance:", balance)
    else:
        print("Insufficient balance!")
else:
    print("Incorrect PIN!")

    
# Build a mini Login system: Username validation, Password validation, OTP Validation.

# Check whether a student passed: Marks ≥ 40, Attendance ≥ 75%

# Scholarship eligibility: Marks ≥ 85, Family income below limit

# Online shopping discount: Purchase amount, Membership status

# Movie ticket pricing based on: Age, Ticket type

# Bank loan approval: Salary criteria, Credit score criteria

# Employee promotion eligibility: Experience, Performance rating

# Admission eligibility: Entrance exam score, Minimum percentage

# Determine tax slab based on income.
