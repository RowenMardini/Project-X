echo "# Project-X" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/RowenMardini/Project-X.git
git push -u origin main
# Calculator Program

def add(x, y):
    """Addition"""
    return x + y

def subtract(x, y):
    """Subtraction"""
    return x - y

def multiply(x, y):
    """Multiplication"""
    return x * y

def divide(x, y):
    """Division"""
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

# User input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter operation number (1-4): ")

if choice == '1':
    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid input. Please enter a valid operation number.")
