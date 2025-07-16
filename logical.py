# A simple calculator app
print('''********************
1. Addition
2. Subtraction
3. Multiplication
4. Division
**************************''')

# ADDITION
print("Enter two numbers to add")
first_number = float(input("first Number: "))
second_number = float(input("second Number: "))
sum = first_number + second_number
print(f"{first_number:.2f} + {second_number:.2f}: {sum:.2f}")

# SUBTRACTION
print("Enter two numbers to sub")
first_number = float(input("first Number: "))
second_number = float(input("second Number: "))
sum = first_number - second_number
print(f"{first_number:.2f} - {second_number:.2f}: {sum:.2f}")

# MULTIPLICATION
print("Enter two numbers to mul")
first_number = float(input("first Number: "))
second_number = float(input("second Number: "))
sum = first_number * second_number
print(f"{first_number:.2f} * {second_number:.2f}: {sum:.2f}")

# DIVISION
print("Enter two numbers to div")
first_number = float(input("first Number: "))
second_number = float(input("second Number: "))
sum = first_number / second_number
print(f"{first_number:.2f} / {second_number:.2f}: {sum:.2f}")

# EXPONENTIAL
print("Enter two numbers to exp")
first_number = float(input("first Number: "))
second_number = float(input("second Number: "))
sum = first_number ** second_number
print(f"{first_number:.2f} ** {second_number:.2f}: {sum}:.22f")


