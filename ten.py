# Function to check if a number is even or odd
def is_even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

# Input a number
number = int(input("Enter a number: "))

# Display if the number is even or odd
print(number, "is", is_even_or_odd(number))
