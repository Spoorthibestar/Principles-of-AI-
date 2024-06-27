# Function to calculate the power of a number
def power(base, exp):
    return base ** exp

# Input base and exponent
base = float(input("Enter the base: "))
exp = float(input("Enter the exponent: "))

# Display the result
print(base, "raised to the power of", exp, "is", power(base, exp))
