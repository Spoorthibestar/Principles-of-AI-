# Function to convert decimal to binary
def decimal_to_binary(n):
    return bin(n).replace("0b", "")

# Input a decimal number
decimal = int(input("Enter a decimal number: "))

# Display the binary representation
print("Binary representation of", decimal, "is", decimal_to_binary(decimal))
