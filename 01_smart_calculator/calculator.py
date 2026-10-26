
# Adds two numbers.
def add(a, b):
    return a + b

# Subtracts the second number from the first.

def subtract(a, b):
    return a - b

# Multiplies two numbers.

def multiply(a, b):
    return a * b

# Divides a by b and handles division by zero.
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b

print("Smart Calculator")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice = input("Enter your choice (1/2/3/4): ")

# Validate menu choice
if choice in ('1', '2', '3', '4'):
    try:
        # Prompt user for numeric inputs and cast to float
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    except ValueError:
        # Handle non-numeric input
        print("Invalid input. Please enter numbers only.")
        
    else:
        # Perform calculation based on choice
        if choice == '1':
            result = add(num1, num2)
            print("Result:", result)
        elif choice == '2':
            result = subtract(num1, num2)
            print("Result:", result)
        elif choice == '3':
            result = multiply(num1, num2)
            print("Result:", result)
        elif choice == '4':
            result = divide(num1, num2)
            print("Result:", result)
else:
    print("Invalid choice.")
