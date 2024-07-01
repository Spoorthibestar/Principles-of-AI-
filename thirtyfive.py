# Function to remove vowels from a string
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in s if char not in vowels)

# Input a string
string = input("Enter a string: ")

# Display the string without vowels
print("String without vowels:", remove_vowels(string))
