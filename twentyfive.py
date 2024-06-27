import math

# Function to check if a number is a perfect square
def is_perfect_square(num):
    root = math.isqrt(num)
    return root * root == num

# Input a number
number = int(input("Enter a number: "))

# Check if the number is a perfect square
if is_perfect_square(number):
    print(number, "is a perfect square")
else:
    print(number, "is not a perfect square")
