# Function to check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# Input a string
string = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(string):
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
