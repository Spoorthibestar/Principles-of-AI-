import random
import string

# Function to generate a random password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Input the desired length of the password
length = int(input("Enter the length of the password: "))

# Display the generated password
print("Generated password:", generate_password(length))
