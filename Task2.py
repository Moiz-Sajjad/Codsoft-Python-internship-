# Function to add two numbers
def Add(x, y):
    return x + y

# Function to subtract two numbers
def Subtract(x, y):
    return x - y

# Function to multiply two numbers
def Multiply(x, y):
    return x * y

# Function to divide
def Divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide a non-zero number by zero"

print("Welcome to the Simple Calculator")

# Input
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))

print("Choose the operation:")
print("Choose a number between 1 to 4")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter the operation number (1/2/3/4): ")

# Perform calculation based on the user's choice
if choice == '1':
    result = Add(num1, num2)
    operator = "+"
elif choice == '2':
    result = Subtract(num1, num2)
    operator = "-"
elif choice == '3':
    result = Multiply(num1, num2)
    operator = "*"
elif choice == '4':
    result = Divide(num1, num2)
    operator = "/"
# If the user enters a number out of range, the else condition is executed
else:
    print("Invalid choice")
    exit()

# Display result
formatted_result = "{:.2f}".format(result) if isinstance(result, float) else result
print(f"{num1} {operator} {num2} = {formatted_result}")
