# Function to count the number of words in a string
def count_words(s):
    return len(s.split())

# Input a string
string = input("Enter a string: ")

# Display the number of words
print("The number of words in the string is:", count_words(string))
