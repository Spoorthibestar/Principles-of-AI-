import math

# Function to calculate LCM
def find_lcm(x, y):
    return abs(x * y) // math.gcd(x, y)

# Input two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Display the LCM
print("The LCM of", num1, "and", num2, "is", find_lcm(num1, num2))
